"""File containing solution attempt for exercise 7.43"""
import math
from ch07.my_practice_implementations.positional_list import PositionalList

def card_shuffle(seq: PositionalList) -> None:
    """
    Describe a method for performing a card shuffle on a list.

    A card shuffle on a list of 2n elements is done by splitting the list 
    into L1 and L2, where L1 is the first half of the list and L2 is the 
    second half of the list. 
    Then, the list is merged back into one by taking the first element in L1,
    followed by the first element in L2, followed by the second element in L1,
    followed by the second element in L2, and so on.
    So for example A, B, C, D, E would become A, D, B, E, C.
    Another way to look at this operation is taking the first half of the list,
    and then inserting elements from the second half of the list between
    consecutive elements of the first half.
    So we have first half A, B, C.
    Second half D, E.
    We insert D between A and B.
    We insert E between B and C.
    """
    length = len(seq)
    if length < 3:
        return
    middle = math.ceil(length / 2) - 1
    walk = seq.first()._node
    pivot = seq.first()._node
    for _ in range(middle):
        pivot = pivot._next

    to_be_inserted = pivot._next
    pivot._next = seq._trailer
    seq._trailer._prev = pivot

    to_be_inserted_count = length - middle - 1 
    for _ in range(to_be_inserted_count):
        after_walk = walk._next
        after_to_be_inserted = to_be_inserted._next

        walk._next = to_be_inserted
        to_be_inserted._prev = walk

        to_be_inserted._next = after_walk
        after_walk._prev = to_be_inserted

        to_be_inserted = after_to_be_inserted
        walk = after_walk

