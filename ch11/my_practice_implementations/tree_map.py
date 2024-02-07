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
from typing import Any, Optional
from ch08.my_practice_implementations import linked_binary_tree
from ch10.my_practice_implementations.map_base import MapBase

K_V_pair = tuple[Any, Any]


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
        It is either the greatest key less than k, or the least key greater 
        than k.
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

    def _relink(
        self,
        parent: linked_binary_tree.Node,
        child: Optional[linked_binary_tree.Node],
        make_left_child: bool = True
    ) -> None:
        """
        Link two given nodes into a parent-child relationship
        """
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p: Position) -> None:
        """
        Rotate position p above its parent
        """
        if p == self.root():
            raise ValueError()
        x = self._validate(p)
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        if x == y._left:
            # relink subtree which is between x and y 
            self._relink(y, x._right, True)
            # swap x and y
            self._relink(x, y, False)
        else:
            # relink subtree which is between x and y
            self._relink(y, x._left, False)
            # swap x and y
            self._relink(x, y, True)

    def _restructure(self, x: Position) -> Position:
        """
        Given a position x, perform a trinode restructuring on x,
        its parent and its grandparent.
        """
        y = self.parent(x)
        z = self.parent(y)
        # nodes have matching alignments, one rotation is sufficient
        if (self.right(y) == x) == (self.right(z) == y):
            self._rotate(y)
            return y
        # non-matching alignments, two rotations needed
        else:
            self._rotate(x)
            self._rotate(x)
            return x

    def first(self) -> Optional[Position]:
        if self.is_empty():
            return None
        return self._subtree_first_position(self.root())

    def last(self) -> Optional[Position]:
        if self.is_empty():
            return None
        return self._subtree_last_position(self.root())

    def before(self, p: Position) -> Optional[Position]:
        if self.left(p) is not None:
            return self._subtree_last_position(self.left())
        walk = p
        above = self.parent(walk)
        while walk is not None and walk == self.left(above):
            walk = above
            above = self.parent(walk)
        return above

    def after(self, p: Position) -> Optional[Position]:
        if self.right(p) is not None:
            return self._subtree_first_position(self.right(p))
        walk = p
        above = self.parent(walk)
        while walk is not None and walk == self.right(above):
            walk = above
            above = self.parent(walk)
        return above

    def find_position(self, k: Any) -> Optional[Position]:
        """
        Return postion containing k if k is in the TreeMap. 
        Otherwise return its neighbour.
        If TreeMap is empty, return None.
        """
        if self.is_empty():
            return None
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p)
        return p

    def find_min(self, p: Position) -> Optional[K_V_pair]:
        ...

    def find_ge(self, k: Any) -> Optional[K_V_pair]:
        """
        Given key k, return its key-value pair if it is in the tree,
        else return the key-value pair whose key is the least key greater than k.
        """

    def find_range(
        self,
        start: Any = None,
        stop: Any = None
    ):
        """
        Produce an iteration of keys start <= k < stop.
        If start is None, minimum key is used as start.
        If stop is None, maxiimum key is used as start.
        """
        if start is None:
            first = self.find_min()
        else:
            first = self.find_position(start)
            if first.key() < start:
                first = self.after(first)
        walk = first
        while walk is not None and (stop is None or walk.key() < stop):
            yield walk.element()
            walk = self.after(walk)

    def __getitem__(self, k: Any) -> Any:
        if self.is_empty():
            raise KeyError()
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p)
        if p.key() != k:
            raise KeyError()
        return p.value()

    def __setitem__(self, k: Any, v: Any) -> None:
        if self.is_empty():
            leaf = self._add_root(self.Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                # existing key, overwrite value
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self.Item(k, v)
                if k > p.key():
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)
            
    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p: Position) -> None:
        """Remove the item at position p"""
        self._validate(p)
        if self.left(p) is not None and self.right(p) is not None:
            replacement = self._subtree_last_position(self.left())
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)


    def __delitem__(self, k: Any) -> None:
        if self.is_empty():
            raise KeyError()
        p = self._subtree_search(self.root(), k)
        if k == p.key():
            self.delete(p)
        else:
            self._rebalance_access(p)
        
    def _rebalance_access(self, p: Position):
        """
        Hook for balanced tree sublasses.
        Rebalance the tree after accessing position p.
        """

    def _rebalance_insert(self, p: Position):
        """
        Hook for balanced tree subclasses.
        Rebalance the tree after inserting position p.
        """

    def _rebalance_delete(self, p: Position):
        """
        Hook for balanced tree subclasses.
        Rebalance the tree after deleting position p.
        """

    