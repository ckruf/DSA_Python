"""
Unit tests for my implementation of the next position methods for exercise 8.50
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from ch08.my_practice_implementations.linked_binary_tree import Position, LinkedBinaryTree


def test_preorder_internal(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    next_pos = bin_tree.preorder_next(F_pos)
    assert next_pos.element() == "B"


def test_preorder_leaf_with_right_sibling(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    D_pos = bin_tree.right(B_pos)
    C_pos = bin_tree.left(D_pos)
    assert C_pos.element() == "C"  # making sure
    next_pos = bin_tree.preorder_next(C_pos)
    assert next_pos.element() == "E"



def test_preorder_leaf_without_right_sibling(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    D_pos = bin_tree.right(B_pos)
    E_pos = bin_tree.right(D_pos)
    assert E_pos.element() == "E"
    next_pos = bin_tree.preorder_next(E_pos)
    assert next_pos.element() == "G"


def test_preorder_last(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    L_pos = bin_tree.right(H_pos)
    M_pos = bin_tree.right(L_pos)
    assert M_pos.element() == "M"
    next_pos = bin_tree.preorder_next(M_pos)
    assert next_pos is None


def test_preorder_single_node():
    bin_tree = LinkedBinaryTree()
    A_pos = bin_tree._add_root("A")
    next_pos = bin_tree.preorder_next(A_pos)
    assert next_pos is None


def test_preorder_two_node():
    bin_tree = LinkedBinaryTree()
    A_pos = bin_tree._add_root("A")
    B_pos = bin_tree._add_left(A_pos, "B")
    assert bin_tree.preorder_next(A_pos).element() == "B"
    assert bin_tree.preorder_next(B_pos) is None

def test_preorder_another_two_node():
    bin_tree = LinkedBinaryTree()
    A_pos = bin_tree._add_root("A")
    B_pos = bin_tree._add_right(A_pos, "B")
    assert bin_tree.preorder_next(A_pos).element() == "B"
    assert bin_tree.preorder_next(B_pos) is None

