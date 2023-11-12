from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Iterator

from ch08.my_practice_implementations.abstract_bin_tree import BinaryTree
from ch08.my_practice_implementations import abstract_tree
from collections import deque



@dataclass(slots=True)
class Node:
    _element: Any
    _parent: Optional[Node]
    _left: Optional[Node]
    _right: Optional[Node]


@dataclass(slots=True)
class Position(abstract_tree.Position):
    _node: Optional[Node]
    _container: LinkedBinaryTree

    def element(self) -> Any:
        return self._node._element

    def __eq__(self, other) -> bool:
        return type(self) is type(other) and self._node is other._node


class LinkedBinaryTree(BinaryTree):
    _root: Optional[Node] = None
    _size: int = 0

    def _validate(self, p: Position) -> Node:
        if not isinstance(p, Position):
            raise TypeError(f"p must be a Position, not {type(p)}")
        if p._container is not self:
            raise ValueError("p is not part of this tree")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node: Optional[Node]) -> Optional[Position]:
        if node is None:
            return None
        return Position(node, self)

    def root(self) -> Optional[Position]:
        return self._root

    def parent(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p: Position) -> int:
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def __len__(self) -> int:
        return self._size

    def left(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._right)

    def _add_root(self, e: Any) -> Position:
        if self._root is not None:
            raise ValueError("tree already has root")
        root_node = Node(e, None, None, None)
        self._root = root_node
        self._size = 1
        return self._make_position(root_node)

    def _add_left(self, p: Position, e: Any) -> Position:
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("p already has left child")
        left_child = Node(e, node, None, None)
        node._left = left_child
        self._size += 1
        return self._make_position(left_child)

    def _add_right(self, p: Position, e: Any) -> Position:
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("p already has right child")
        right_child = Node(e, node, None, None)
        node._right = right_child
        self._size += 1
        return self._make_position(right_child)

    def _replace(self, p: Position, e: Any) -> Any:
        node = self._validate(p)
        original = node._element
        node._element = e
        return original

    def _delete(self, p: Position) -> Any:
        """
        Delete given node and replace it with its child, if it has a child.
        Raise ValueError if the given node has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Cannot delete node with two children")
        child = node._left or node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(
        self,
        p: Position,
        t1: Optional[LinkedBinaryTree],
        t2: Optional[LinkedBinaryTree]
    ) -> None:
        """
        Attach 
        - tree t1 as left child of given position
        - tree t2 as right child of given position
        
        Note that the left and/or right child position must be empty if you
        want to attach tree.

        Attaching the trees will empty the original trees.
        """
        node = self._validate(p)
        if not type(self) is type(t1) is type(t2):
            raise TypeError("t1 and t2 must be LinkedBinaryTree instances")
        size_t1 = len(t1) if t1 is not None else 0
        size_t2 = len(t2) if t2 is not None else 0
        if t1 is not None and not t1.is_empty():
            if self.left(p) is not None:
                raise ValueError("given position can't have left child if you want to attach t1")
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
            
        if t2 is not None and not t2.is_empty():
            if self.right(p) is not None:
                raise ValueError("given position can't have right child if you want to attach t2")
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
        
        self._size += (size_t1 + size_t2)

    def positions(self) -> Iterator[Position]:
        return self.inorder()