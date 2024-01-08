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

def test_post_order_right_child(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    G_pos = bin_tree.right(F_pos)
    next_pos = bin_tree.postorder_next(G_pos)
    assert next_pos.element() == "F"

def test_post_order_single_left_child():
    bin_tree = LinkedBinaryTree()
    A_pos = bin_tree._add_root("A")
    B_pos = bin_tree._add_left(A_pos, "B")
    next_pos = bin_tree.postorder_next(B_pos)
    assert next_pos.element() == "A"

def test_post_order_left_child_with_childfree_sibling(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    next_pos = bin_tree.postorder_next(B_pos)
    assert next_pos.element() == "G"


def test_post_order_left_child_with_sibling(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    next_pos = bin_tree.postorder_next(F_pos)
    assert next_pos.element() == "I"


def test_post_order_root(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    assert bin_tree.postorder_next(H_pos) is None


def test_post_order_right_sibling():
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
    bin_tree._add_right(J_pos, "K")
    bin_tree._add_right(L_pos, "M")
    assert bin_tree.postorder_next(F_pos).element() == "K"


def test_post_order_right_sibling_2():
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
    bin_tree._add_right(L_pos, "M")
    assert bin_tree.postorder_next(F_pos).element() == "M"


def test_inorder_left_child_without_right_child(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    A_pos = bin_tree.left(B_pos)
    next_pos = binary_tree_first_example.inorder_next(A_pos)
    assert next_pos.element() == "B"


def test_inorder_left_child_with_right_child(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    next_pos = bin_tree.inorder_next(H_pos)
    assert next_pos.element() == "I"


def test_inorder_right_child(binary_tree_first_example):
    bin_tree: LinkedBinaryTree = binary_tree_first_example
    H_pos = bin_tree.root()
    F_pos = bin_tree.left(H_pos)
    B_pos = bin_tree.left(F_pos)
    D_pos = bin_tree.right(B_pos)
    E_pos = bin_tree.right(D_pos)
    next_pos = bin_tree.inorder_next(E_pos)
    assert next_pos.element() == "F"
