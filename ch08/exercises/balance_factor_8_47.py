"""
The balance factor of an internal position p of a proper binary tree is the
difference between the heights of the right and left subtrees of p. Show
how to specialize the Euler tour traversal of Section 8.4.6 to print the
balance factors of all the internal nodes of a proper binary tree.
"""

import sys
import os
from pathlib import Path
from typing import Any

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from typing import Union
from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree, Position, Node
from ch08.exercises.euler_tour_applications import create_non_positioned_bin_tree, create_binary_expression_tree
from ch08.my_practice_implementations.euler_tour import BinaryEulerTour


def compute_balance_factor(tree: LinkedBinaryTree) -> int:
    def _recurse(p: Position, depth: int) -> int:
        left_subtree_depth = depth
        right_subtree_depth = depth
        left_pos = tree.left(p)
        if left_pos is not None:
            left_child_depth = _recurse(left_pos, depth+1)
            if left_child_depth > left_subtree_depth:
                left_subtree_depth = left_child_depth
        right_pos = tree.right(p)
        if right_pos is not None:
            right_child_depth = _recurse(right_pos, depth+1)
            if right_child_depth > right_subtree_depth:
                right_subtree_depth = right_child_depth
        balance_factor = right_subtree_depth - left_subtree_depth
        print(f"balance factor for {p.element()} is {balance_factor}")
        return max(left_subtree_depth, right_subtree_depth)
    root_pos = tree.root()
    _recurse(root_pos, 0)


class BalanceFactorTour(BinaryEulerTour):


    def _hook_postvisit(self, p: Position, d: int, path: list[int], results: list) -> Any:
        # Compute the height of the left and right children
        left_height = results[0] if results[0] is not None else 0
        right_height = results[1] if results[1] is not None else 0

        # Calculate the balance factor
        balance_factor = left_height - right_height
        print(f"Balance factor for {p.element()} is {balance_factor}")

        # Return the height of the current node
        return max(left_height, right_height) + 1



if __name__ == "__main__":
    tree = create_non_positioned_bin_tree()
    balance_tour = BalanceFactorTour(tree)
    balance_tour.execute()
