import pytest

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.parent.absolute()
print("src_dir", src_dir)
sys.path.insert(0, str(src_dir))

from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree


@pytest.fixture()
def binary_tree_first_example():
    """
    Fixture to create an example binary tree.
    This tree is based on the tree in Figure 8.22, but has been filled in with
    letters of the alphabet, starting at 'A', going in an inorder traversal.
    """
    bin_tree = LinkedBinaryTree()
    root_pos = bin_tree._add_root("H")
    F_pos = bin_tree._add_left(root_pos, "F")
    B_pos = bin_tree._add_left(F_pos, "B")
    bin_tree._add_left(B_pos, "A")
    D_pos = bin_tree._add_right(B_pos, "D")
    bin_tree._add_left(D_pos, "C")
    bin_tree._add_right(D_pos, "E")
    bin_tree._add_right(F_pos, "G")
    L_pos = bin_tree._add_right(root_pos, "L")
    J_pos = bin_tree._add_left(L_pos, "J")
    bin_tree._add_left(J_pos, "I")
    bin_tree._add_right(J_pos, "K")
    bin_tree._add_right(L_pos, "M")
    return bin_tree