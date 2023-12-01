"""
Unit tests for my implementation of the swap method for exercise 8.39
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from typing import Any
from ch08.my_practice_implementations.linked_binary_tree import Position, LinkedBinaryTree


def test_non_adjacent_same_parent(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    L_pos = bin_tree.right(H_pos)
    elements_before = [p.element() for p in bin_tree.inorder()]
    bin_tree._swap(F_pos, L_pos)
    elements = [p.element() for p in bin_tree.inorder()]
    assert elements == [
        "I", "J", "K", "L", "M", "H", "A", "B", "C", "D", "E"
    ]
    bin_tree._swap(F_pos, L_pos)
    assert [p.element() for p in bin_tree.inorder()] == elements_before

def test_non_adjacent_same_parent_leaf(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    G_pos = bin_tree.right(F_pos)
    elements_before = [p.element() for p in bin_tree.inorder()]
    bin_tree._swap(B_pos, G_pos)
    elements = [p.element() for p in bin_tree.inorder()]
    assert elements == [
        "G", "F", "A", "B", "C", "D", "E", "H", "I", "J", "K", "L", "M"
    ]
    bin_tree._swap(B_pos, G_pos)
    assert elements_before == [p.element() for p in bin_tree.inorder()]


def test_non_adjacent_different_parent(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    L_pos = bin_tree.right(H_pos)
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    J_pos = bin_tree.left(L_pos)
    elements_before = [p.element() for p in bin_tree.inorder()]
    bin_tree._swap(B_pos, J_pos)
    elements = [p.element() for p in bin_tree.inorder()]
    assert elements == [
        "I", "J", "K", "F", "G", "H", "A", "B", "C", "D", "E", "L", "M"
    ]
    bin_tree._swap(B_pos, J_pos)
    assert elements_before == [p.element() for p in bin_tree.inorder()]


def test_adjacent(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    elements_before = [p.element() for p in bin_tree.inorder()]
    bin_tree._swap(B_pos, F_pos)
    elements = [p.element() for p in bin_tree.inorder()]
    assert elements == [
        "F", "G", "A", "B", "C", "D", "E", "H", "I", "J", "K", "L", "M"
    ]
    bin_tree._swap(B_pos, F_pos)
    assert elements_before == [p.element() for p in bin_tree.inorder()]

def test_adjacent_reverse_order(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    elements_before = [p.element() for p in bin_tree.inorder()]
    bin_tree._swap(F_pos, B_pos)
    elements = [p.element() for p in bin_tree.inorder()]
    assert elements == [
        "F", "G", "A", "B", "C", "D", "E", "H", "I", "J", "K", "L", "M"
    ]
    bin_tree._swap(F_pos, B_pos)
    assert elements_before == [p.element() for p in bin_tree.inorder()]
