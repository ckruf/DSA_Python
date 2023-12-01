"""
Provide an algorithm for computing the number of descendants of each node of
a binary tree. The algorithm should be based on the Euler tour traversal.
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from typing import Any
from ch08.my_practice_implementations.linked_binary_tree import Position
from ch08.my_practice_implementations.euler_tour import BinaryEulerTour
from ch08.exercises.euler_tour_applications import create_binary_tree


class ComputeDescendantsTour(BinaryEulerTour):
    
    def _hook_postvisit(self, p: Position, d: int, path: list[int], results: list) -> Any:
        sub_total = sum(filter(lambda x: x is not None, results))
        print(f"number of descendants for {p.element().element} is {sub_total}")      
        return sub_total + 1


def main():
    bin_tree = create_binary_tree()
    descendants_tour = ComputeDescendantsTour(bin_tree)
    descendants_tour.execute()


if __name__ == "__main__":
    main()