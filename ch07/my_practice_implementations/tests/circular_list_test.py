import pytest
from ch07.my_practice_implementations.circular_list import (
    CircularList,
    Node
)


class TestInsertFirst:
    """
    Tests for the 'insert_first()' method of the CircularList class.
    """

    @staticmethod
    def insert_into_empty_list():
        test_list = CircularList()
        
        assert len(test_list) == 0
        assert test_list._tail is None

        test_list.insert_first("A")
        assert len(test_list) == 1
        A_node = test_list._tail
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert test_list._tail._next == A_node

    @staticmethod
    def insert_into_single_element_list():
        test_list = CircularList()
        B_node = Node("B")
        B_node._next = B_node
        test_list._tail = B_node
        test_list._size = 1

        test_list.insert_first("A")

        A_node = test_list._tail._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node
        assert test_list._tail == B_node

    @staticmethod
    def insert_into_multi_element_list():
        test_list = CircularList()
        C_node = Node("C")

