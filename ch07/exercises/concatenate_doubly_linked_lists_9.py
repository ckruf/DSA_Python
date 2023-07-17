"""This file contains solution attempt for exercise 7.9"""
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


def concatenate_doubly_linked(
    first: PositionalList,
    second: PositionalList
) -> None:
    """
    Give a fast algorithm for concatenating two doubly linked lists L and M,
    with header and trailer sentinel nodes, into a single list L'
    
    This function will change the 'first' list to become the result of 
    the concatenation, and empty out the second list.
    """
    if len(second) == 0:
        return
    
    last_elem_first = first._trailer._prev
    trailer_first = first._trailer

    first_elem_second = second._header._next
    last_elem_second = second._trailer._prev
    header_second = second._header
    trailer_second = second._trailer

    last_elem_first._next = first_elem_second
    trailer_first._prev = last_elem_second
    
    first_elem_second._prev = last_elem_first
    last_elem_second._next = trailer_first
    
    header_second._next = trailer_second
    trailer_second._prev = header_second

    first._size += second._size
    second._size = 0

if __name__ == "__main__":
    first = PositionalList()
    second = PositionalList()
    first_elems = ["A", "B", "C",]
    second_elems = ["D", "E", "F"]
    for e in first_elems:
        first.add_last(e)
    for e in second_elems:
        second.add_last(e)
    assert first_elems == [e for e in first]
    assert second_elems == [e for e in second]
    assert len(first) == 3
    assert len(second) == 3
    concatenate_doubly_linked(first, second)
    walk = first._header
    while walk is not None:
        print(walk)
        walk = walk._next
    assert [e for e in first] == first_elems.extend(second)
    assert [e for e in second] == second_elems
    assert len(first) == 6
    assert len(second) == 3
