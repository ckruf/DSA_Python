"""This file contains tests for exercise 7.5"""
from ch07.my_practice_implementations.circular_list import CircularList
from ch07.exercises.count_circular_5 import count_nodes_circular


def test_count_nodes_empty():
    test_list = CircularList()
    assert count_nodes_circular(test_list) == 0


def test_count_nodes_single_element():
    test_list = CircularList()
    test_list.insert_last("A")
    assert count_nodes_circular(test_list) == 1


def test_count_nodes_mulitple_elements():
    test_list = CircularList()
    elems = ["A", "B", "C"]
    for e in elems:
        test_list.insert_last(e)
    assert count_nodes_circular(test_list) == len(elems)


def test_count_nodes_circular_50():
    """
    Tests the 'count_nodes_circular()' function. Test by adding 50 items
    one by one and checking the count after each added element.
    This therefore covers all the classic cases (empty, one element,
    mulitple elements).
    NOTE however that this test also relies on the correct impolementation
    of the 'CircularList' class. Unit tests for that class are separate
    in a different file.
    """
    test_list = CircularList()
    for i in range(50):
        assert len(test_list) == count_nodes_circular(test_list) == i
        if i % 2 == 0:
            test_list.insert_last(i)
        else:
            test_list.insert_first(i)
    for i in range(49, 0, -1):
        if i % 2 == 0:
            test_list.delete_first()
        else:
            test_list.delete_last()
        assert len(test_list) == count_nodes_circular(test_list) == i
