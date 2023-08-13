"""File containing tests for exercise 7.36"""
from ch07.exercises.positional_list_no_sentinels_36 import (
    PositionalList,
    Position,
    Node
)
import pytest


class TestAddFirst:
    """
    Tests for the 'add_first()' method of the PositionalList class.
    """

    @staticmethod
    def test_add_first_empty():
        test_list = PositionalList()
        assert len(test_list) == 0
        assert test_list._first == test_list._last == None
        
        A_pos = test_list.add_first("A")
        
        assert len(test_list) == 1
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        A_node = A_pos._node
        assert A_node == test_list._first
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node._prev == None
        assert test_list._last == A_node

    @staticmethod
    def test_add_first_non_empty():
        test_list = PositionalList()
        C_pos = test_list.add_first("C")
        assert len(test_list) == 1
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"
        C_node = C_pos._node
        assert C_node == test_list._first
        assert isinstance(C_node, Node)
        assert C_node._element == "C"
        assert C_node._next == C_node._prev == None

        B_pos = test_list.add_first("B")
        assert len(test_list) == 2
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        B_node = B_pos._node
        assert B_node == test_list._first
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == C_node
        assert B_node._prev is None

        assert C_node._prev == B_node
        assert C_node._next is None
        assert test_list._last == C_node

        A_pos = test_list.add_first("A")
        assert len(test_list) == 3
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        A_node = A_pos._node 
        assert A_node == test_list._first
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node
        assert A_node._prev is None
        
        assert B_node._prev == A_node
        assert test_list._last == C_node


class TestAddLast:
    """
    Tests for the 'add_last()' method of the PositionalList class.
    """

    @staticmethod
    def test_add_last_empty():
        test_list = PositionalList()
        assert len(test_list) == 0
        assert test_list._first == test_list._last == None
        
        A_pos = test_list.add_last("A")
        assert len(test_list) == 1
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        A_node = A_pos._node
        assert A_node == test_list._first
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node._prev == None
        assert test_list._last == A_node

    @staticmethod
    def test_add_last_non_empty():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        assert len(test_list) == 1
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        A_node = A_pos._node
        assert A_node == test_list._first
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node._prev == None

        B_pos = test_list.add_last("B")
        assert len(test_list) == 2
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        B_node = B_pos._node
        assert B_node == test_list._last
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._prev == A_node
        assert B_node._next is None

        assert A_node == test_list._first
        assert A_node._next == B_node
        assert A_node._prev is None

        C_pos = test_list.add_last("C")
        assert len(test_list) == 3
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"
        C_node = C_pos._node
        assert C_node == test_list._last
        assert isinstance(C_node, Node)
        assert C_node._element == "C"
        assert C_node._prev == B_node
        assert C_node._next is None

        assert B_node._next == C_node


class TestAddAfter:
    """
    Tests for the 'add_after()' method of the PositionalList class.
    """

    @staticmethod
    def test_add_after():
        test_list = PositionalList()
        test_list.add_last("A")
        test_list.add_last("C")
        assert len(test_list) == 2

        A_node = test_list._first
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        
        C_node = test_list._last
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        assert A_node._prev is None
        assert A_node._next == C_node

        assert C_node._prev == A_node
        assert C_node._next is None

        A_pos = test_list.first()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"

        B_pos = test_list.add_after(A_pos, "B")

        assert len(test_list) == 3
        
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"

        B_node = B_pos._node
        assert isinstance(B_node, Node)
        
        assert B_node._next == C_node
        assert B_node._prev == A_node

        assert A_node._next == B_node
        assert C_node._prev == B_node


    @staticmethod
    def test_add_after_last():
        test_list = PositionalList()
        test_list.add_last("A")
        assert len(test_list) == 1
        A_node = test_list._last 
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node._prev == None

        A_pos = test_list.first()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"

        B_pos = test_list.add_after(A_pos, "B")

        assert isinstance(B_pos, Position)
        B_node = B_pos._node
        assert isinstance(B_node, Node)
        assert B_node == test_list._last
        assert B_node._element == "B"
        assert B_node._prev == A_node
        assert B_node._next is None



class TestAddBefore:
    """
    Tests for the 'add_before()' method of the PositionalList class.
    """

    @staticmethod
    def test_add_before():
        test_list = PositionalList()
        test_list.add_last("A")
        test_list.add_last("C")
        assert len(test_list) == 2

        A_node = test_list._first
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        
        C_node = test_list._last
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        assert A_node._prev is None
        assert A_node._next == C_node

        assert C_node._prev == A_node
        assert C_node._next is None

        C_pos = test_list.last()
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"

        B_pos = test_list.add_before(C_pos, "B")

        assert len(test_list) == 3

        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        B_node = B_pos._node
        assert isinstance(B_node, Node)
        
        assert B_node._next == C_node
        assert B_node._prev == A_node

        assert A_node._next == B_node
        assert C_node._prev == B_node


    @staticmethod
    def test_add_before_first():
        test_list = PositionalList()
        test_list.add_last("B")
        B_node = test_list._first
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == B_node._prev == None
        assert len(test_list) == 1
        B_pos = test_list.first()
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"

        A_pos = test_list.add_before(B_pos, "A")
        assert len(test_list) == 2
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        A_node = A_pos._node
        assert isinstance(A_node, Node)
        assert A_node == test_list._first
        assert A_node._element == "A"
        assert A_node._prev is None
        assert A_node._next == B_node


class TestDeleteFirst:
    """
    Tests for the 'delete_first()' method of the PositionalList class.
    """

    @staticmethod
    def test_delete_first_empty():
        test_list = PositionalList()
        with pytest.raises(Exception):
            test_list.delete_first()

    @staticmethod
    def test_delete_first_single_element():
        test_list = PositionalList()
        test_list.add_first("A")

    @staticmethod
    def test_delete_first_two_elements():
        pass

    @staticmethod
    def test_delete_first():
        pass