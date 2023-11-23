"""
File containing test(s) for exercise 8.5
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from ch08.exercises.left_children_8_5 import left_child_leaves


def test_left_child_leaves(
    binary_tree_first_example
):
    tree = binary_tree_first_example
    assert left_child_leaves(tree) == 3