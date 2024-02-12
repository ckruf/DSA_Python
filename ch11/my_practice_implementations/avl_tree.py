from __future__ import annotations
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))

from dataclasses import dataclass
from typing import Optional
from .tree_map import TreeMap, Position


@dataclass(slots=True)
class Node:
    _left: Optional[Node]
    _right: Optional[Node]
    _parent: Optional[Node]
    _element: Optional[TreeMap.Item]
    _height: int = 0

    def left_height(self) -> int:
        return self._left._height if self._left is not None else 0

    def right_height(self) -> int:
        return self._right._height if self._right is not None else 0


class AVLTree(TreeMap):
    
    def _recompute_height(self, p: Position) -> None:
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _is_balanced(self, p: Position) -> bool:
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self, p: Position, favor_left: bool = False) -> Position:
        left_child_height = p._node.left_height()
        right_child_height = p._node.right_height()
        if left_child_height > right_child_height:
            return self.left(p)
        elif right_child_height > left_child_height:
            return self.right(p)
        else:
            return self.left(p) if favor_left else self.right(p)

    def _tall_grandchild(self, p: Position) -> Position:
        tall_child = self._tall_child(p)
        # in case of equally tall children, favor same side
        favor_left = tall_child == self.left(p)
        return self._tall_child(tall_child, favor_left)

    def _rebalance(self, p: Position) -> None:
        """
        Recompute the heights of nodes after an insertion/deletion,
        and rebalance the tree if necessary
        """     
        while p is not None:
            old_height = p._node._height
            if not self._is_balanced(p):
                self._restructure(self._tall_grandchild(p))
                # trinode restructure could have changed heights
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if old_height == p._node._height:
                p = None
            else:
                p = self.parent(p)

    def _rebalance_delete(self, p: Position):
        self._rebalance(p)

    def _rebalance_insert(self, p: Position):
        self._rebalance(p)