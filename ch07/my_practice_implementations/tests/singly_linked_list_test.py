"""
Tests for the LinkedList class, implementing a singly linked list.
"""

import pytest
from unittest.mock import MagicMock

from ch07.my_practice_implementations.singly_linked_list import LinkedList, Node


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
        - size incremented
        - self._head._next set to None
        - self._tail set correctly!!!
        """
        test_list = LinkedList()
        assert test_list._head is None
        assert test_list._tail is None
        assert len(test_list) == 0

        test_list.add_first("A")
        assert isinstance(test_list._head, Node)
        assert test_list._head._element == "A"
        assert test_list._head._next is None
        assert test_list._tail == test_list._head
        assert len(test_list) == 1

    @staticmethod
    def test_add_first_non_empty():
        """
        Test that the 'add_first()' method correctly adds node in case of
        initially non-empty list. Check the following:
        - self._head set correctly
        - size incremented
        - self._head._next set to original head
        """
        test_list = LinkedList()
        test_list.add_first("B")
        B_node = test_list._head
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert len(test_list) == 1

        test_list.add_first("A")
        A_node = test_list._head
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node
        assert len(test_list) == 2


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
        test_list = LinkedList()
        assert test_list._head is None
        assert test_list._tail is None
        assert len(test_list) == 0

        test_list.add_last("A")
        assert isinstance(test_list._head, Node)
        assert test_list._head._element == "A"
        assert test_list._head._next is None
        assert test_list._tail == test_list._head
        assert len(test_list) == 1

    @staticmethod
    def test_add_last_non_empty():
        """
        Test thtat the 'add_last()' method correctly adds node in case of
        initially non-empty list. Check the following:
        - self._tail set to new node
        - ._next of old tail set to new tail/new node
        - size incremented
        """
        test_list = LinkedList()
        test_list.add_last("A")
        A_node = test_list._tail
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None

        test_list.add_last("B")
        B_node = test_list._tail
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert A_node._next == B_node
        assert len(test_list) == 2


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
        test_list = LinkedList()
        elems = ["A", "C", "D"]
        for e in elems:
            test_list.add_last(e)

        A_node = test_list._head
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        C_node = A_node._next
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        assert len(test_list) == 3

        test_list.add_at_index("B", 1)

        B_node = A_node._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == C_node

        assert len(test_list) == 4

    @staticmethod
    def test_add_at_middle_index():
        """
        Test that the 'add_at_index()' method correctly inserts at index
        of a middle node (ie excluding indices 0, 1, -1, -2).
        Check the same stuff as the previous test
        """
        test_list = LinkedList()
        elems = ["A", "B", "D", "E"]
        for e in elems:
            test_list.add_last(e)
        B_node = test_list._head._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        D_node = B_node._next
        assert isinstance(D_node, Node)
        assert D_node._element == "D"

        assert len(test_list) == 4

        test_list.add_at_index("C", 2)

        C_node = B_node._next
        assert isinstance(C_node, Node)
        assert C_node._element == "C"
        assert C_node._next == D_node
        assert len(test_list) == 5

    @staticmethod
    def test_raises_exception_negative_index():
        """
        Test that the 'add_at_index()' method raises an Exception when
        it is given index less than 0.
        """
        test_list = LinkedList()
        with pytest.raises(Exception):
            test_list.add_at_index("A", -1)

    @staticmethod
    def test_raises_exception_excessive_index():
        """
        Test that the 'add_at_index()' method raises an Exception when
        it is given an index greater than the length of the list.
        """
        test_list = LinkedList()
        test_list.add_last("A")
        with pytest.raises(Exception):
            test_list.add_at_index("B", 2)

    @staticmethod
    def test_calls_appropriate_method_first():
        """
        Test that the 'add_at_index()' method calls 'add_first()'
        method when given the corresponding index.
        """
        test_list = LinkedList()
        test_list.add_first = MagicMock()
        test_list.add_at_index("A", 0)
        test_list.add_first.assert_called_once_with("A")

    @staticmethod
    def test_calls_appropriate_method_last():
        """
        Test that the 'add_at_index()' method calls 'add_last()' method when
        given the corresponding index.
        """
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)
        test_list.add_last = MagicMock()
        test_list.add_at_index("D", 3)
        test_list.add_last.assert_called_once_with("D")


class TestDeleteFirst:
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
        - node is deprecated by setting its attributes to None
        """
        test_list = LinkedList()
        test_list.add_first("A")

        assert len(test_list) == 1
        A_node = test_list._head
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert test_list._tail == A_node

        element = test_list.delete_first()
        assert element == "A"
        assert len(test_list) == 0
        assert test_list._head is None
        assert test_list._tail is None
        assert A_node._element is None
        assert A_node._next is None

    @staticmethod
    def test_multiple_element_list():
        """
        Test that the 'delete_first()' method correctly removes the first
        element of the list when the list contains multiple elements.
        Check the following:
        - self._head is correctly updated
        - self._size is decremented
        - return value is correct
        - node is deprecated by setting its attributes to None
        """
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)

        assert len(test_list) == 3
        A_node = test_list._head
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        element = test_list.delete_first()
        assert element == "A"
        assert len(test_list) == 2
        B_node = test_list._head
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        assert A_node._element is None
        assert A_node._next is None

    @staticmethod
    def test_empty_list():
        """
        Test that the 'delete_first()' raises an Exception when called
        on an empty list.
        """
        test_list = LinkedList()
        with pytest.raises(Exception):
            test_list.delete_first()


class TestDeleteLast:
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
        test_list = LinkedList()
        test_list.add_last("A")
        A_node = test_list._head
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert test_list._tail == A_node
        assert len(test_list) == 1

        element = test_list.delete_last()
        assert element == "A"
        assert len(test_list) == 0
        assert test_list._head is None
        assert test_list._tail is None

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
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)
        assert len(test_list) == 3
        C_node = test_list._tail
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        element = test_list.delete_last()
        assert element == "C"
        B_node = test_list._tail
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next is None
        assert len(test_list) == 2
        assert C_node._element is None
        assert C_node._next is None

    @staticmethod
    def test_empty_list():
        """
        Test that the 'delete_last()' method raises an Exception when called
        on an empty list.
        """
        test_list = LinkedList()
        with pytest.raises(Exception):
            test_list.delete_last()


class TestDeleteAtIndex:
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
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)
        # get all three nodes
        A_node = test_list._head
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        B_node = A_node._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        C_node = B_node._next
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        assert len(test_list) == 3

        element = test_list.delete_at_index(1)

        assert element == "B"
        assert A_node._next == C_node
        assert len(test_list) == 2
        assert B_node._next is None
        assert B_node._element is None

    @staticmethod
    def test_delete_at_illegal_index():
        """
        Test that the 'delete_at_index()' method raises Exception when it
        is given an illegal index
        """
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)
        with pytest.raises(Exception):
            test_list.delete_at_index(3)

    @staticmethod
    def test_calls_appropriate_method_first():
        """
        Test that the 'delete_at_index()' method calls 'add_first()'
        method when given the corresponding index.
        """
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)
        test_list.delete_first = MagicMock()
        test_list.delete_at_index(0)
        test_list.delete_first.assert_called_once_with()

    @staticmethod
    def test_calls_appropriate_method_last():
        """
        Test that the 'delete_at_index()' method calls 'add_last()' method
        when given the corresponding index.
        """
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)
        test_list.delete_last = MagicMock()
        test_list.delete_at_index(2)
        test_list.delete_last.assert_called_once_with()


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
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)
        assert test_list.get_first() == "A"

    @staticmethod
    def test_get_first_empty():
        """
        Test that the 'get_first()' method raises an Exception when called
        on an empty list.
        """
        test_list = LinkedList()
        with pytest.raises(Exception):
            test_list.get_first()


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
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)
        assert test_list.get_last() == "C"

    @staticmethod
    def test_get_last_empty():
        """
        Test that the 'get_last()' method raises an Exception when called
        on an empty list.
        """
        test_list = LinkedList()
        with pytest.raises(Exception):
            test_list.get_last()


class TestGetAtIndex:
    """
    Tests for the 'get_node_at_index()' and 'get_element_at_index()' methods.
    """

    @staticmethod
    def test_get_node_at_index():
        test_list = LinkedList()
        for e in ("A", "B", "C"):
            test_list.add_last(e)
        A_node = test_list._head
        B_node = A_node._next
        C_node = B_node._next

        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        assert test_list.get_node_at_index(0) == A_node
        assert test_list.get_node_at_index(1) == B_node
        assert test_list.get_node_at_index(2) == C_node

    @staticmethod
    def test_get_element_at_index():
        test_list = LinkedList()
        for e in ("A", "B", "C"):
            test_list.add_last(e)
        A_node = test_list._head
        B_node = A_node._next
        C_node = B_node._next

        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        assert test_list.get_element_at_index(0) == "A"
        assert test_list.get_element_at_index(1) == "B"
        assert test_list.get_element_at_index(2) == "C"


class TestIter:
    """
    Tests for the __iter__ method of the LinkedList class.
    """

    @staticmethod
    def test_iter():
        """
        Test the __iter__ method on an non-empty list.
        """
        elems = ["A", "B", "C", "D"]
        test_list = LinkedList()
        for e in elems:
            test_list.add_last(e)
        for list_value, linked_list_value in zip(elems, test_list):
            assert list_value == linked_list_value
        assert elems == [e for e in test_list]

    @staticmethod
    def test_iter_empty():
        """
        Test that the __iter__ method works on an empty list.
        """
        test_list = LinkedList()
        for e in test_list:
            assert False
        assert True


class TestStr:
    """
    Test for the __str__ method of the LinkedList class.
    """

    @staticmethod
    def test_str():
        elems = ["A", "B", "C"]
        test_list = LinkedList()
        for e in elems:
            test_list.add_last(e)
        assert str(test_list) == str(elems)


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
        test_list = LinkedList()
        for e in ["A", "B", "C"]:
            test_list.add_last(e)

        # get all three nodes
        A_node = test_list._head
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        B_node = A_node._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        C_node = B_node._next
        assert isinstance(C_node, Node)
        assert C_node._element == "C"
        assert test_list._tail == C_node

        assert len(test_list) == 3

        test_list.clear()

        assert test_list._head is None
        assert test_list._tail is None
        assert len(test_list) == 0

        assert A_node._element is None
        assert A_node._next is None

        assert B_node._element is None
        assert B_node._next is None

        assert C_node._element is None
        assert C_node._next is None
