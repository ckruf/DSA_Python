import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from typing import Any, Optional
from ch08.my_practice_implementations.euler_tour import BinaryEulerTour
from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree, Position
from ch08.exercises.euler_tour_applications import create_binary_tree


class LevelNumberTour(BinaryEulerTour):

    def _hook_previsit(self, p: Position, d: int, path: list[int]) -> None:
        current_total = 0
        for i in path:
            current_total *= 2
            if i == 0:
                current_total += 1
            elif i == 1:
                current_total += 2
            else:
                raise ValueError()
        print(current_total)


def test_level_number_tour():
    bin_tree = create_binary_tree()
    level_tour = LevelNumberTour(bin_tree)
    level_tour.execute()


if __name__ == "__main__":
    test_level_number_tour()
