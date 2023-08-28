"""File containing tests for exercise 7.37"""
from ch07.exercises.two_sum_positional_list_37 import (
    PositionalList,
    two_sum_sorted as two_sum
)


def test_two_sum_existing():
    """
    Test the two sum functions. Cases tested:
    - existing sum 
    - first and last element sum
    - non existing sum
    """
    test_list = PositionalList()
    elems = [1, 4, 5, 7, 10, 20, 27, 28, 29]
    for e in elems:
        test_list.add_last(e)
    four_pos = test_list.find(4)
    twenty_pos = test_list.find(20)
    assert two_sum(test_list, 24) == (four_pos, twenty_pos)

def test_two_sum_first_and_last():
    test_list = PositionalList()
    elems = [1, 4, 5, 7, 20, 27, 28, 29]
    for e in elems:
        test_list.add_last(e)
    one_pos = test_list.first()
    twenty_nine_pos = test_list.last()
    assert two_sum(test_list, 30) == (one_pos, twenty_nine_pos)


def test_two_sum_non_existing():
    test_list = PositionalList()
    elems = [1, 4, 5, 7, 10, 20, 27, 28, 29]
    for e in elems:
        test_list.add_last(e)
    assert two_sum(test_list, 60) is None


def test_two_sum_empty_list():
    test_list = PositionalList()
    assert two_sum(test_list, 0) is None


def test_two_sum_two_element_list():
    test_list = PositionalList()
    one_pos = test_list.add_last(1)
    five_pos = test_list.add_last(5)
    assert two_sum(test_list, 6) == (one_pos, five_pos)
    assert two_sum(test_list, 10) is None