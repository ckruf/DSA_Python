"""File containing solution attempt for exercise 7.38"""
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.absolute()
dsa_python_dir = src_dir.parent.absolute()
sys.path.insert(0, str(dsa_python_dir))

from ch07.my_practice_implementations.positional_list import PositionalList
from ch07.exercises.swap_nodes_4 import swap_neighboring_nodes_doubly_linked


def bubble_sort(elements: PositionalList) -> None:
    """
    Use bubble sort to sort positional list (doubly linked list).
    """
    for i in range(len(elements) - 1):
        first_in_comparison_pair = elements.first()
        second_in_comparison_pair = elements.after(first_in_comparison_pair)
        for _ in range(len(elements) - 1 - i):
            if first_in_comparison_pair.element() > second_in_comparison_pair.element():
                swap_neighboring_nodes_doubly_linked(
                    first_in_comparison_pair._node,
                    second_in_comparison_pair._node
                )
                second_in_comparison_pair = elements.after(first_in_comparison_pair)
            else:
                first_in_comparison_pair = second_in_comparison_pair
                second_in_comparison_pair = elements.after(second_in_comparison_pair)


if __name__ == "__main__":
    test_list = PositionalList()
    elements = [5, 1, 7, 2, 4]
    for e in elements:
        test_list.add_last(e)
    print("test_list: ", test_list)
    bubble_sort(test_list)
    print("test list:", test_list)