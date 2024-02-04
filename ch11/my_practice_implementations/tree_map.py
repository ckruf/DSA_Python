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
from typing import Any
from ch08.my_practice_implementations import linked_binary_tree
from ch10.my_practice_implementations.map_base import MapBase


@dataclass(slots=True)
class Position(linked_binary_tree.Position):

    def key(self) -> Any:
        return self.element()._key

    def value(self) -> Any:
        return self.element()._value



class TreeMap(linked_binary_tree.LinkedBinaryTree, MapBase):
    """
    Sorted map implementation using binary tree.
    Also serves as a base class for subclasses implementing tree balancing.
    """

    def _subtree_search(self, p: Position, k: Any) -> Position:
        """
        Given key k, search the (sub)tree for the key.
        If k is in the tree, return the position at which it is found.
        Otherwise, return the last position searched. (Useful for __setitem__,
        because that is the position where k will be attached).
        """
        if k == p.key():
            return p
        elif k < p.key() and self.left(p) is not None:
            return self._subtree_search(self.left(p), k)
        elif k > p.key() and self.right(p) is not None:
            return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p: Position) -> Position:
        """
        Return Position of first item of subtree rooted at p.
        Meaning the first position in terms of order of the keys, so the 
        leftmost position in the tree.
        Basically, just keep walking left.
        """
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p: Position) -> Position:
        """The opposite of _subtree_first_position"""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk