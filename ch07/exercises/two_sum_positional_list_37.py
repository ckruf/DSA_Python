"""
File containing solution attempt for exercise 7.37.

This exercise is to implement two-sum on a sorted PositionalList.

The only idea that comes to my mind is to use a dictionary. Iterate over
the elements. Store each element in a dictionary, the value of the element
being the dict key and the associated Position being the dict value. And for 
each element check whether the result of (target - current_element) is stored
in the dict.

However it feels like this solution is not really taking advantage of the fact
that the list is sorted.

One way which I thought of is that rather than storing items in a dict,
we could just binary search the list for the remaining value, but as far 
as I can tell, binary search won't really work on a linked sequence, since
it requires indexing into the middle position in the list.

Correction/addition:

The right approach, which takes advantage of the fact that the list is sorted,
is to put a pointer at each end of the list and check if the elements add up to 
the sum. If they add up to a lower number, advance the pointer at the start
of the list. If they add up to a higher number, decrement the pointer at the 
end of the list.
"""
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.absolute()
dsa_python_dir = src_dir.parent.absolute()
sys.path.insert(0, str(dsa_python_dir))

from typing import Any, Optional, Tuple
from ch07.my_practice_implementations.positional_list import PositionalList, Position


def two_sum(
    elements: PositionalList, target: Any
) -> Optional[Tuple[Position, Position]]:
    """
    Given a sorted list of items, and a target value, determine whether the 
    list contains two elements which sum to the target value. Return the 
    two positions if two such elements exists, otherwise return None.
    The positions will be returned in the order in which they appear in the list.
    """
    values_and_positions = {}
    if elements.is_empty():
        return None
    walk = elements.first()
    while walk is not None:
        elem = walk.element()
        remainder = target - elem
        possible_position = values_and_positions.get(remainder)
        if possible_position is not None:
            return possible_position, walk
        values_and_positions[elem] = walk
        walk = elements.after(walk)
    return None


def two_sum_sorted(
    elements: PositionalList, target: Any
) -> Optional[Tuple[Position, Position]]:
    """
    Given a sorted list of items, and a target value, determine whether the 
    list contains two elements which sum to the target value. Return the 
    two positions if two such elements exists, otherwise return None.
    The positions will be returned in the order in which they appear in the list.
    """
    if elements.is_empty():
        return None
    low_pointer = elements.first()
    high_pointer = elements.last()
    while low_pointer != high_pointer:
        sum = low_pointer.element() + high_pointer.element()
        if sum == target:
            return low_pointer, high_pointer
        elif sum < target:
            low_pointer = elements.after(low_pointer)
        elif sum > target:
            high_pointer = elements.before(high_pointer)
    return None