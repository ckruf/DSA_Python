"""This file contains tests for exercise 7.1"""
from ch07.exercises.find_penultimate_node_1 import (
    find_penultimate_node_recursive as find_penultimate_node,
)
from ch07.my_practice_implementations.singly_linked_list import LinkedList, Node


class TestFindPenultimateNode:
    """
    Tests for the 'find_penultimate_node()' function - exercise 7.1.
    NOTE: these tests are dependent on a correct implementation of
    the LinkedList class, which has its own tests separately.
    """

    @staticmethod
    def test_find_penultimate_nonexistent():
        """
        Test that 'find_penultimate_node()' returns None when there is no
        penultimate node - when length is 0 or 1.
        """
        test_list = LinkedList()
        penultimate = find_penultimate_node(test_list)
        assert penultimate is None
        test_list.add_last("A")
        penultimate = find_penultimate_node(test_list)
        assert penultimate is None

    @staticmethod
    def test_find_penultimate_two_elements():
        """
        Test that 'find_penultimate_node()' returns the correct node
        when the linked list contains two elements.
        """
        test_list = LinkedList()
        test_list.add_last("A")
        test_list.add_last("B")
        penultimate = find_penultimate_node(test_list)
        assert isinstance(penultimate, Node)
        assert penultimate.element() == "A"
        assert penultimate == test_list._head

    @staticmethod
    def test_find_penultimate_mulitple_elements():
        """
        Test that 'find_penultimate_node()' returns the correct node
        when the linked list contains more than two elements.
        """
        test_list = LinkedList()
        elements = ["A", "B", "C", "D"]
        for e in elements:
            test_list.add_last(e)
        penultimate = find_penultimate_node(test_list)
        assert isinstance(penultimate, Node)
        assert penultimate.element() == "C"
        assert penultimate == test_list._head._next._next
