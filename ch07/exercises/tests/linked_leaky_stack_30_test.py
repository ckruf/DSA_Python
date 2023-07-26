"""This file contains tests for exercise 7.30"""
import pytest
from ch07.exercises.linked_leaky_stack_30 import LinkedLeakyStack, Node


class TestInit:
    """Tests for the __init__() method of the LinkedLeakyStack class."""

    @staticmethod
    def test_init_no_capacity():
        test_stack = LinkedLeakyStack()
        assert test_stack._capacity == LinkedLeakyStack.DEFAULT_SIZE
        assert test_stack._top is None
        assert test_stack._size == 0

    @staticmethod
    def test_init_valid_capacity():
        test_stack = LinkedLeakyStack(10)
        assert test_stack._capacity == 10
        assert test_stack._top is None
        assert test_stack._size == 0

    @staticmethod
    def test_init_invalid_capacity():
        with pytest.raises(Exception):
            test_stack = LinkedLeakyStack(0)


class TestPush:
    """Tests for the 'push()' method of the LinkedLeakyStack class."""

    @staticmethod
    def test_push_empty_stack():
        test_stack = LinkedLeakyStack()
        assert test_stack._top is None
        assert test_stack._size == len(test_stack) == 0
        test_stack.push("A")
        A_node = test_stack._top
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None
        assert test_stack._size == len(test_stack) == 1

    @staticmethod
    def test_push_non_empty_non_full_stack():
        test_stack = LinkedLeakyStack()
        test_stack.push("B")
        test_stack.push("A")
        assert test_stack._size == len(test_stack) == 2
        A_node = test_stack._top
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        B_node = A_node._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

    @staticmethod
    def test_push_non_empty_full_stack():
        test_stack = LinkedLeakyStack(3)
        for e in "D", "C", "B":
            test_stack.push(e)
        assert len(test_stack) == test_stack._size == 3
        B_node = test_stack._top
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        C_node = B_node._next
        assert isinstance(C_node, Node)
        assert C_node._element == "C"
        D_node = C_node._next
        assert isinstance(D_node, Node)
        assert D_node._element == "D"

        test_stack.push("A")
        
        A_node = test_stack._top
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node
        assert B_node._next == C_node
        assert C_node._next is None
        assert len(test_stack) == test_stack._size == 3

    @staticmethod
    def test_push_full_stack_capacity_1():
        test_stack = LinkedLeakyStack(1)
        test_stack.push("B")
        B_node = test_stack._top
        assert isinstance(test_stack._top, Node)
        assert B_node._element == "B"
        assert B_node._next is None
        assert len(test_stack) == 1
        test_stack.push("A") 
        A_node = test_stack._top
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None
        assert len(test_stack) == 1