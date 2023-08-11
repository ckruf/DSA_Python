"""This file contains solution attempt for exercise 7.8"""
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.absolute()
dsa_python_dir = src_dir.parent.absolute()
sys.path.insert(0, str(dsa_python_dir))

from ch07.my_practice_implementations.positional_list import PositionalList, _Node


def find_middle_node(dl_list: PositionalList) -> _Node:
    """
    Describe a nonrecursive method for ﬁnding, by link hopping, the middle
    node of a doubly linked list with header and trailer sentinels. In the case
    of an even number of nodes, report the node slightly left of center as the
    “middle.” (Note: This method must only use link hopping; it cannot use a
    counter.) What is the running time of this method?
    """
    if len(dl_list) == 0:
        raise ValueError("The list is empty")
    elif len(dl_list) == 1:
        return dl_list._header._next
    else:
        left = dl_list._header
        right = dl_list._trailer
        while left != right and left != right._prev:
            print("left", left)
            print("right", right)
            print("left == right", left == right)
            left = left._next
            right = right._prev
        return left


if __name__ == "__main__":
    test_list = PositionalList()
    for e in "A", "B", "C":
        test_list.add_last(e)
    middle_node = find_middle_node(test_list)
    print("middle_node", middle_node)
