from __future__ import annotations
from abc import ABCMeta
from dataclasses import dataclass
from typing import Any, Iterator, List, Optional
from ch08.my_practice_implementations import abstract_tree


@dataclass(slots=True)
class Node:
    _element: Any
    _parent: Optional[Node]
    _children: List[Node]


@dataclass(slots=True)
class Position(abstract_tree.Position):
    _node: Optional[Node]
    _container: LinkedTree

    def element(self) -> Any:
        return self._node._element

    def __eq__(self, other) -> bool:
        return type(self) is type(other) and self._node is other._node


@dataclass()
class LinkedTree(abstract_tree.Tree):
    _root: Optional[Node] = None
    _size: int = 0

    def _make_position(self, node: Optional[Node]) -> Optional[Position]:
        if node is None:
            return None
        return Position(node, self)

    def _validate(self, p: Optional[Position]) -> Node:
        if not isinstance(p, Position):
            raise TypeError(f"p must be a Position instance, not {type(p)}")
        if p._container is not self:
            raise ValueError("p must belong to this tree")
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def root(self) -> Optional[Position]:
        return self._make_position(self._root)

    def parent(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p: Position) -> int:
        node = self._validate(p)
        return len(node._children)

    def children(self, p: Position) -> Iterator[Position]:
        node = self._validate(p)
        for c in node._children:
            yield self._make_position(c)

    def __len__(self) -> int:
        return self._size
    
    def add_root(self, e: Any) -> Position:
        if not self.is_empty():
            raise ValueError("The tree must be empty when adding a root")
        self._root = Node(e, None, [])
        self._size = 1
        return self._make_position(self._root)
    
    def add_child(self, p: Position, e: Any) -> Position:
        node = self._validate(p)
        new_child = Node(e, node, [])
        node._children.append(new_child)
        self._size += 1
        return self._make_position(new_child)
    
    def add_child_at(self, p: Position, e: Any, index: int) -> Position:
        """
        Add a child at the given index .
        """
        node = self._validate(p)
        if not (0 <= index <= len(node._children)):
            raise ValueError(f"the given index must be between 0 and {len(node._children)}  incl")
        child = Node(e, node, [])
        node._children.insert(index, child)
        self._size += 1
        return self._make_position(child)
    
    def replace(self, p: Position, e: Any) -> Any:
        node = self._validate(p)
        original_element = node._element
        node._element = e
        return original_element
    
    def delete(self, p: Position) -> Any:
        """
        Delete the node at position p, and return the element.
        If p has single child, replace p with the child.
        If p has multiple children, raise error.
        """ 
        node = self._validate(p)
        if len(node._children) > 1:
            raise ValueError("cannot delete node with mulitple children")
        elif len(node._children) == 1:
            child = node._children[0]
            parent = node._parent
            node._children = None
            node._parent = node
            element = node._element
            node._element = None
            for i in range(len(parent._children)):
                if parent._children[i] == node:
                    parent._children[i] = child
                    break
        # doesn't have children
        else:
            parent = node._parent
            if parent:
                parent._children.remove(node)
            # convention for deprecated nodes
            node._parent = node
            element = node._element
            node._element = None
            node._children = None
        
        return element
