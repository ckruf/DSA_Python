"""
Tests for the LinkedList class, implementing a singly linked list.
"""

import pytest

from ch07.my_practice_implementations.singly_linked_list import (
    LinkedList,
    Node
)


class TestAddFirst:
    """
    Tests for 'add_first()' method of LinkedList class.
    """

    @staticmethod
    def test_add_first_empty():
        """
        Test that the 'add_first()' method correctly adds node in case
        of initially empty list. Check the following:
        - self._head set correctly
        - size incrementd
        - self._head._next set to None
        - self._tail set correctly!!!
        """

    @staticmethod
    def test_add_first_non_empty():
        """
        Test that the 'add_first()' method correctly adds node in case of 
        initially non-empty list. Check the following:
        - self._head set correctly
        - size incremented
        - self._head._next set to original head
        """

class TestAddLast:
    """
    Tests for the 'add_last()' method of the LinkedList class.
    """

    @staticmethod
    def test_add_last_empty():
        """
        Test that the 'add_last()' method correctly adds node in case of
        initially empty list. Check the following:
        - self._tail set to new node
        - self._head set to new node
        - size incremented
        """

    @staticmethod
    def test_add_last_non_empty():
        """
        Test thtat the 'add_last()' method correctly adds node in case of 
        initially non-empty list. Check the following:
        - self._tail set to new node
        - ._next of old tail set to new tail/new node
        - size incremented
        """


class TestAddAtIndex:
    """
    Tests for the 'add_at_index()' method of the LinkedList class.
    Test cases for adding at first and last position are not included,
    because for those cases the method just calls the 'add_first()' and
    'add_last()' methods anyway.
    """

    @staticmethod
    def test_add_at_second_index():
        """
        Test that the 'add_at_index()' method correctly inserts at index 1.
        Check the following:
        - count is incremented
        - ._next of preceding node is correctly updated
        - ._next of newly inserted node is correctly set
        - size is incremented
        """

    @staticmethod
    def test_add_at_middle_index():
        """
        Test that the 'add_at_index()' method correctly inserts at index
        of a middle node (ie excluding indices 0, 1, -1, -2).
        Check the same stuff as the previous test
        """

    @staticmethod
    def test_raises_exception_illegal_index():
        """
        Test that the 'add_at_index()' method raises an Exception when 
        it is given index less than 0 or greater than length.
        """

    @staticmethod
    def test_calls_appropriate_methods_first_last():
        """
        Test that the 'add_at_index()' method calls 'add_first()' and 
        'add_last()' methods when given the corresponding indices.
        """


class DeleteFirst:
    """
    Tests for the 'delete_first()' method of the LinkedList class.
    """

    @staticmethod
    def test_single_element_list():
        """
        Test that the 'delete_first()' method correctly removes the first 
        element of the list when the list contains a single element.
        Check the following:
        - self._head is set to None
        - self._tail is set to None
        - self._size is decremented to 0
        - return value is correct
        """

    @staticmethod
    def test_multiple_element_list():
        """
        Test that the 'delete_first()' method correctly removes the first
        element of the list when the list contains multiple elements.
        Check the following:
        - self._head is correctly updated
        - self._size is decremented
        - return value is correct
        """

    @staticmethod
    def test_empty_list():
        """
        Test that the 'delete_first()' raises an Exception when called 
        on an empty list.
        """


class DeleteLast:
    """
    Tests for the 'delete_last()' method of the LinkedList class.
    """

    @staticmethod
    def test_single_element_list():
        """
        Test that the 'delete_last()' method correctly removes the last
        element of the list when the list contains a single element.
        Check the following:
        - self._head is set to None
        - self._tail is set to None
        - self._size is decremented to 0
        - return value is correct
        """

    @staticmethod
    def test_multiple_element_list():
        """
        Test that the 'delete_last()' method correctly removes the last element
        of the list when the list contains multiple elements.
        Check the following:
        - self._tail is correctly set to preceding element
        - self._tail._next is set to None
        - self._size is decremented
        - return value is correct
        """

    @staticmethod
    def test_empty_list():
        """
        Test that the 'delete_last()' method raises an Exception when called
        on an empty list.
        """


class DeleteAtIndex:
    """
    Tests for the 'delete_at_index()' method of the LinkedList class.
    Test cases for deleting first or last position are not included, because
    for those cases, the method just calls 'delete_first()' and 'delete_last()'
    """

    @staticmethod
    def test_delete_at_index():
        """
        Test that the 'delete_at_index()' method correctly removes node at given
        index.
        Check the following:
        - preceding node's ._next is correctly updated
        - return value is correct
        - self._size is decremented
        """

    @staticmethod
    def test_delete_at_illegal_index():
        """
        Test that the 'delete_at_index()' method raises Exception when it 
        is given an illegal index
        """

    @staticmethod
    def test_calls_appropriate_methods_first_last():
        """
        Test that the 'delete_at_index()' method calls 'add_first()' and 
        'add_last()' methods when given the corresponding indices.
        """


class TestGetFirst:
    """
    Tests for the 'get_first()' method of the LinkedList class.
    """

    @staticmethod
    def test_get_first_existent():
        """
        Test that the 'get_first()' method correctly returns the first 
        element, when the list is not empty.
        """

    @staticmethod
    def test_get_first_empty():
        """
        Test that the 'get_first()' method raises an Exception when called
        on an empty list.
        """


class TestGetLast:
    """
    Tests for the 'get_last()' method of the LinkedList class.
    """

    @staticmethod
    def test_get_last_existent():
        """
        Test that the 'get_last()' method correctly returns the last item
        in the list, when the list is not empty.
        """


    @staticmethod
    def test_get_last_empty():
        """
        Test that the 'get_last()' method raises an Exception when called
        on an empty list.
        """


class TestIter:
    """
    Tests for the __iter__ method of the LinkedList class.
    """

    @staticmethod
    def test_iter():
        """
        Test the __iter__ method on an non-empty list.
        """

    @staticmethod
    def test_iter_empty():
        """
        Test that the __iter__ method works on an empty list.
        """


class TestStr:
    """
    Test for the __str__ method of the LinkedList class.
    """

    @staticmethod
    def test_str():
        pass


class TestClear:
    """
    Tests for the 'clear()' method of the LinkedList class.
    """

    @staticmethod
    def test_clear():
        """
        Test that the 'clear()' method clears the lists and enables
        garbage collection of the nodes.
        Check the following: 
        - self._head is set to None
        - self._tails is set to None
        - self._size is set to 0
        - all the nodes have their ._element and ._next set to None
        """