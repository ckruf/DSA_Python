"""This file contains tests for exercise 7.3"""
from ch07.my_practice_implementations.singly_linked_list import LinkedList
from ch07.exercises.count_nodes_recursive_3 import count_nodes

def test_count_nodes():
    """
    Test the 'count_nodes()' function.
    """
    test_list = LinkedList()
    elems = ("A", "B", "C", "D")
    for e in elems:
        test_list.add_last(e)
    assert count_nodes(test_list) == len(elems)

def test_count_nodes_single():
    """
    Test the 'count_nodes()' function on a single element list.
    """
    test_list = LinkedList()
    test_list.add_last("A")
    assert count_nodes(test_list) == 1


def test_count_nodes_empty():
    """
    Test the 'count_nodes()' function on an empty list.
    """
    test_list = LinkedList()
    assert count_nodes(test_list) == 0