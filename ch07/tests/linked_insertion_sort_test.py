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

def insertion_sort_attempt_1(seq: PositionalList):
    """
    Attempt at insertion sort on a doubly linked list. The reason that this 
    implementation does not work is the advancing of the 'marker' variable.

    Suppose you have a list [2, 1].
    to_be_inserted points to the Position containing 1.
    marker and walk point to the Position containing 2.
    The condition while walk != seq.first()... does not get executed even
    once, because walk does in fact equal seq.first().
    We add 1 before 2, such that we temporarily have a list [1, 2, 1].
    We delete the 1 after the 2, such that we get the list [1, 2].
    We then set marker = seq.after(marker).
    The problem is that market is already pointing to the last element of the
    list. So marker = seq.after(marker) will set marker to None.
    The outer while loop will execute again, because marker != seq.last(),
    as it is None.
    This will then cause an Exception.
    """
    if len(seq) < 2:
        return
    
    marker = seq.first()
    while marker != seq.last():
        to_be_inserted = seq.after(marker)
        walk = marker
        while walk != seq.first() and to_be_inserted.element() < walk.element():
            walk = seq.before(walk)
        seq.add_before(walk, to_be_inserted.element())
        seq.delete(to_be_inserted)
        marker = seq.after(marker)

def insertion_sort_attempt_2(seq: PositionalList):
    if len(seq) < 2:
        return
    
    marker = seq.first()
    while marker != seq.last():
        to_be_inserted = seq.after(marker)
        value_to_be_inserted = to_be_inserted.element()
        walk = to_be_inserted
        while walk != seq.first() and value_to_be_inserted < seq.before(walk).element():
            walk = seq.before(walk)
        seq.add_before(walk, to_be_inserted.element())
        seq.delete(to_be_inserted)
        marker = seq.after(marker)

def insertion_sort_attempt_3(seq: PositionalList):
    if len(seq) < 2:
        return
    
    marker = seq.first()
    while marker is not None:
        to_be_inserted = seq.after(marker)
        value_to_be_inserted = to_be_inserted.element()
        walk = to_be_inserted
        while walk != seq.first() and value_to_be_inserted < seq.before(walk).element():
            walk = seq.before(walk)
        seq.add_before(walk, to_be_inserted.element())
        seq.delete(to_be_inserted)
        marker = seq.after(marker)


class TestLinkedInsertionSort:
    """
    Tests for insertion sort algorithm done on doubly linked list implemented
    as the PositionalList class/API.
    """

    @staticmethod
    def test_two_element_list():
        test_list = PositionalList()
        test_list.add_last(2)
        test_list.add_last(1)
        assert [2, 1] == [i for i in test_list]
        # insertion_sort(test_list)
        assert [1, 2] == [i for i in test_list]


if __name__ == "__main__":
    test_list = PositionalList()
    # elements = [15, 22, 25,]
    elements = [25, 22, 15]
    for elem in elements:
        test_list.add_last(elem)
    print("test list before sorting", test_list)
    insertion_sort_attempt_3(test_list)
    print("test list after sorting", test_list)
    