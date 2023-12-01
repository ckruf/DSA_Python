"""
Design an algorithm that tests whether two given ordered trees are isomorphic.
What is the running time of your algorithm?
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from ch08.my_practice_implementations.linked_tree import LinkedTree, Position
from ch08.exercises.euler_tour_applications import create_non_positioned_bin_tree, create_binary_expression_tree

def is_isomorphic(T1: LinkedTree, T2: LinkedTree) -> bool:
    def recurse(p1: Position, p2: Position) -> bool:
        if T1.num_children(p1) == T2.num_children(p2):
            for c1, c2 in zip(T1.children(p1), T2.children(p2)):
                if not recurse(c1, c2):
                    return False
            return True
        else:
            return False

    return recurse(T1.root(), T2.root())
