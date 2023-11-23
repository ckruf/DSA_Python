"""
File containing solution attempt for exercise 8.5
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree, \
    Position
from ch08.exercises.euler_tour_applications import create_binary_tree


def left_child_leaves(bin_tree: LinkedBinaryTree) -> int:
    """
    Count the number of leaf positions in a binary tree,
    which are the left child of their parent.
    """

    def _recurse(p: Position, is_left: bool) -> int:
        sub_total = 0
        if bin_tree.num_children(p) == 0:
            if is_left:
                return 1
            else:
                return 0
        if bin_tree.left(p) is not None:
            sub_total += _recurse(bin_tree.left(p), True)
        if bin_tree.right(p) is not None:
            sub_total += _recurse(bin_tree.right(p), False)
        return sub_total

    
    return _recurse(bin_tree.root(), False)



if __name__ == "__main__":
    tree = create_binary_tree()
    print("left leaves are:", left_child_leaves(tree))