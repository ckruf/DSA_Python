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
    def test_insert_into_empty_list():
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
    def test_insert_into_single_element_list():
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
        assert len(test_list) == 2

    @staticmethod
    def test_insert_into_multi_element_list():
        test_list = CircularList()
        C_node = Node("C")
        B_node = Node("B")
        C_node._next = B_node
        B_node._next = C_node
        test_list._tail = C_node
        test_list._size = 2

        test_list.insert_first("A")
        A_node = C_node._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node
        assert test_list._tail == C_node
        assert len(test_list) == 3


class TestInsertLast:
    """
    Tests for the 'insert_last()' method of the CircularList class.
    """

    @staticmethod
    def test_insert_into_empty_list():
        test_list = CircularList()
        
        assert len(test_list) == 0
        assert test_list._tail is None

        test_list.insert_last("A")

        A_node = test_list._tail
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node
        assert len(test_list) == 1

    @staticmethod
    def test_insert_into_single_element_list():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._size = 1
        test_list._tail = A_node

        test_list.insert_last("B")
        B_node = test_list._tail
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == A_node
        assert len(test_list) == 2

    @staticmethod
    def test_insert_into_multi_element_list():
        test_list = CircularList()
        A_node = Node("A")
        B_node = Node("B")

        B_node._next = A_node
        A_node._next = B_node
        test_list._tail = B_node
        test_list._size = 2

        test_list.insert_last("C")
        C_node = test_list._tail
        assert isinstance(C_node, Node)
        assert C_node._element == "C"
        assert C_node._next == A_node
        assert B_node._next == C_node
        assert len(test_list) == 3


class TestInsertAfter:

    @staticmethod
    def test_insert_after_only_node():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._tail = A_node
        test_list._size = 1
        
        test_list.insert_after(A_node, "B")

        B_node = test_list._tail._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert A_node._next == B_node
        assert B_node._next == A_node
        assert len(test_list) == 2 

    @staticmethod
    def test_insert_after_mulitple_nodes():
        pass