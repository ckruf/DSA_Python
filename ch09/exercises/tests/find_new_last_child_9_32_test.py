import pytest

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from typing import Optional
from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree, Position
from ch09.my_practice_implementations.priority_queue_base import Item


class LastPositionTree(LinkedBinaryTree):
    _last_position: Optional[Position]

    def set_last_position(self, p: Position) -> None:
        self._last_position = p

    def get_last_position(self) -> Optional[Position]:
        return self._last_position

    def update_last_position_after_adding(self):
        """
        Assuming that self._last_position is the last position in a heap before adding a new position,
        come up with a O(log(n)) algorithm to find the new last position after adding.
        The idea is to walk up the tree, until we can find either 1) a point where we can 'turn right',
        Meaning that we find a node which has a right child which was not part of the path walking up.
        Or 2) until we get to the root (this will only be the case when the new last node is the first node on a new level).
        Then, once we've 'turned right' or reached the root, we start walking down and left, until we reach a leaf node.
        That's the new last position.
        """
        if self.is_empty():
            self._last_position = self._root
            return
        p = self._last_position
        # going up until we can go right or until we reach root
        # the order of this condition is actually important, opposite order can cause error
        while not self.is_root(p) and self.right(self.parent(p)) == p:
            p = self.parent(p)
        if not self.is_root(p):
            p = self.right(self.parent(p))
        while not self.is_leaf(p):
            p = self.left(p)
        self._last_position = p


def test_left_child_is_last():
    """
    Test that _last_position is correctly updated when the _last_position before
    add() is a left child. Therefore, the new last position will just be the new right sibling.
    The tree used is based on the heap in Figure 9.1 of Goodrich.
    """
    tree = LastPositionTree()
    # root
    C_element = tree._add_root(Item(4, "C"))
    # level 1
    A_element = tree._add_left(C_element, Item(5, "A"))
    Z_element = tree._add_right(C_element, Item(6, "Z"))
    # level 2
    K_element = tree._add_left(A_element, Item(15, "K"))
    F_element = tree._add_right(A_element, Item(9, "F"))
    Q_element = tree._add_left(Z_element, Item(7, "Q"))
    B_element = tree._add_right(Z_element, Item(20, "B"))
    # level 3
    X_element = tree._add_left(K_element, Item(16, "X"))
    
    tree.set_last_position(X_element)
    J_element = tree._add_right(K_element, Item(25, "J"))
    tree.update_last_position_after_adding()
    assert tree.get_last_position() == J_element


def test_right_child_is_last_same_half():
    """
    Test that _last_position is correctly updated when the _last_position before
    add() is a right child, and the new last position is in the same half of the tree.
    Therefore it is not necessary to go all the way up to the root.
    """
    tree = LastPositionTree()
    # root
    C_element = tree._add_root(Item(4, "C"))
    # level 1
    A_element = tree._add_left(C_element, Item(5, "A"))
    Z_element = tree._add_right(C_element, Item(6, "Z"))
    # level 2
    K_element = tree._add_left(A_element, Item(15, "K"))
    F_element = tree._add_right(A_element, Item(9, "F"))
    Q_element = tree._add_left(Z_element, Item(7, "Q"))
    B_element = tree._add_right(Z_element, Item(20, "B"))
    # level 3
    X_element = tree._add_left(K_element, Item(16, "X"))
    J_element = tree._add_right(K_element, Item(25, "J"))

    tree.set_last_position(J_element)
    E_element = tree._add_left(F_element, Item(14, "E"))
    tree.update_last_position_after_adding()
    assert tree.get_last_position() == E_element


def test_right_child_is_last_other_half():
    """
    Test that _last_position is correctly updated when the _last_postiion before
    add() is a right child, and the new last position is in the other half of the tree.
    Therefore, it is necessary to go all the way up to the root, and then down.
    """
    tree = LastPositionTree()
    # root
    C_element = tree._add_root(Item(4, "C"))
    # level 1
    A_element = tree._add_left(C_element, Item(5, "A"))
    Z_element = tree._add_right(C_element, Item(6, "Z"))
    # level 2
    K_element = tree._add_left(A_element, Item(15, "K"))
    F_element = tree._add_right(A_element, Item(9, "F"))
    Q_element = tree._add_left(Z_element, Item(7, "Q"))
    B_element = tree._add_right(Z_element, Item(20, "B"))
    # level 3
    X_element = tree._add_left(K_element, Item(16, "X"))
    J_element = tree._add_right(K_element, Item(25, "J"))
    E_element = tree._add_left(F_element, Item(14, "E"))
    H_element = tree._add_right(F_element, Item(12, "H"))

    tree.set_last_position(H_element)
    S_element = tree._add_left(Q_element, Item(11, "S"))
    tree.update_last_position_after_adding()
    assert tree.get_last_position() == S_element


def test_new_last_child_is_on_next_level():
    """
    Test that the _last_position is correctly updated when the _last_postiion before 
    add() is the last possible position on the given level, and the new last position
    will be on a new level.
    """
    tree = LastPositionTree()
    # root
    C_element = tree._add_root(Item(4, "C"))
    # level 1
    A_element = tree._add_left(C_element, Item(5, "A"))
    Z_element = tree._add_right(C_element, Item(6, "Z"))
    # level 2
    K_element = tree._add_left(A_element, Item(15, "K"))
    F_element = tree._add_right(A_element, Item(9, "F"))
    Q_element = tree._add_left(Z_element, Item(7, "Q"))
    B_element = tree._add_right(Z_element, Item(20, "B"))
    # level 3
    X_element = tree._add_left(K_element, Item(16, "X"))
    J_element = tree._add_right(K_element, Item(25, "J"))
    E_element = tree._add_left(F_element, Item(14, "E"))
    H_element = tree._add_right(F_element, Item(12, "H"))
    S_element = tree._add_left(Q_element, Item(11, "S"))
    W_element = tree._add_right(Q_element, Item(13, "W"))
    T_element = tree._add_left(B_element, Item(22, "T"))
    U_element = tree._add_right(B_element, Item(23, "U"))

    tree.set_last_position(U_element)
    Y_element = tree._add_left(X_element, Item("Y", 30))
    tree.update_last_position_after_adding()
    assert tree.get_last_position() == Y_element
