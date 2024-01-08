"""File containing my implementation of a linked binary tree"""
from __future__ import annotations

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

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
    
    def __ne__(self, other) -> bool:
        return not (self == other)


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
        return self._make_position(self._root)

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

    def _delete_subtree(self, p: Position) -> None:
        """
        Delete the subtree rooted at position p (including p):
        - update _size
        - set node._parent to node to indicate that the node
        is deprecated 
        - set left, right and element to None, for garbage collection
        I wonder whether this has to be done as a postorder traversal,
        or whether it can be done as a preorder traversal...
        """
        def _recurse_delete(p: Position) -> int:
            sub_total = 0
            for c in self.children(p):
                sub_total += _recurse_delete(c)
            node = self._validate(p)
            node._left = None
            node._right = None
            node._element = None
            node._parent = node
            return sub_total + 1

        if p == self.root():
            self._root = None
        else:
            parent = self.parent(p)
            parent_node = self._validate(parent)
            if self.left(parent) == p:
                parent_node._left = None
            elif self.right(parent) == p:
                parent_node._right = None
        deleted_count = _recurse_delete(p)
        self._size -= deleted_count

    def preorder_next(self, p: Position) -> Optional[Position]:
        if self.num_children(p) > 0:
            if self.left(p):
                return self.left(p)
            return self.right(p)
        has_right_sibling = False
        while not has_right_sibling:
            parent = self.parent(p)
            if parent is None:
                return None
            has_right_sibling = self.left(parent) == p and self.right(parent) is not None
            if has_right_sibling:
                return self.right(parent)
            p = parent
            parent = self.parent(parent)

    def postorder_next(self, p: Position) -> Optional[Position]:
        parent = self.parent(p)
        # root
        if parent is None:
            return None
        parents_right = self.right(parent)
        # last child on this level -> return parent
        if p == parents_right or parents_right is None:
            return parent
        # has childless right sibling
        if self.num_children(parents_right) == 0:
            return parents_right
        # has right sibling with children
        return self._dig_deep_prefer_left(parents_right)

    def _dig_deep_prefer_left(self, p: Position) -> Position:
        """
        Given a position, find its deepest child when prefering left children.
        """
        if self.num_children(p) == 0:
            return p
        left_child = self.left(p)
        right_child = self.right(p)
        if left_child is not None:
            return self._dig_deep_prefer_left(left_child)
        return self._dig_deep_prefer_left(right_child)

    def _find_left_ancestor(self, p: Position) -> Optional[Position]:
        """
        Given a position, find its nearest ancestor who is a left child.
        """
        if p is None or self.parent(p) is None:
            return None
        parent = self.parent(p)
        if p == self.left(parent):
            return p
        return self._find_left_ancestor(parent)

    def inorder_next(self, p: Position) -> Optional[Position]:
        parent = self.parent(p)
        # root
        if parent is None:
            return self._dig_deep_prefer_left(self.right(p))
        # if position is a left child
        if p == self.left(parent):
            if self.right(p) is None:
                return self.parent(p)
            return self._dig_deep_prefer_left(p)
        # position is a right child
        if self.right(p) is not None:
            return self.right(p)
        nearest_left_ancestor =  self._find_left_ancestor(parent)
        if nearest_left_ancestor is not None:
            return self.parent(nearest_left_ancestor)
        return None
