"""
Unit tests for my implementation of the delete subtree method for exercise 8.38
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


def test_second_level_internal(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    original_size = len(bin_tree)
    H_pos = bin_tree.root()
    L_pos = bin_tree.right(H_pos)
    J_pos = bin_tree.left(L_pos)
    elements = [p.element() for p in bin_tree.inorder()]
    print(elements)
    assert "J" in elements
    assert "I" in elements
    assert "K" in elements
    bin_tree._delete_subtree(J_pos)
    elements = [p.element() for p in bin_tree.inorder()]
    print(elements)
    assert "J" not in elements
    assert "I" not in elements
    assert "K" not in elements
    assert len(bin_tree) == original_size - 3


def test_root(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    root = bin_tree.root()
    bin_tree._delete_subtree(root)
    assert len(bin_tree) == 0
    assert bin_tree.root() is None
    assert [p for p in bin_tree.positions()] == []

def test_leaf(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    G_pos = bin_tree.right(F_pos)
    original_len = len(bin_tree)
    elements = [p.element() for p in bin_tree.positions()]
    assert G_pos.element() in elements
    bin_tree._delete_subtree(G_pos)
    elements = [p.element() for p in bin_tree.positions()]
    assert G_pos.element() not in elements
    assert len(bin_tree) == original_len - 1

