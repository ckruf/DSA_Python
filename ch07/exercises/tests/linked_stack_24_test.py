"""This file contains tests for exercise 7.24"""
import pytest
from ch07.exercises.linked_stack_24 import Node, LinkedStack


class TestPush:
    """
    Tests for the 'push()' method of the LinkedStack class.
    """

    @staticmethod
    def test_push_empty():
        test_stack = LinkedStack()
        assert isinstance(test_stack._header, Node)
        assert test_stack._header._next is None
        assert len(test_stack) == 0
        test_stack.push("A")
        A_node = test_stack._header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None
        assert len(test_stack) == 1

    @staticmethod
    def test_push_non_empty():
        test_stack = LinkedStack()
        test_stack.push("A")
        assert isinstance(test_stack._header, Node)
        A_node = test_stack._header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None
        assert len(test_stack) == 1
        test_stack.push("B")
        B_node = test_stack._header._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == A_node
        assert A_node._next is None
        assert len(test_stack) == 2


class TestPop:
    """
    Tests for the 'pop()' method of the LinkedStack class.
    """

    @staticmethod
    def test_pop_empty():
        test_stack = LinkedStack()
        with pytest.raises(Exception):
            test_stack.pop()

    @staticmethod
    def test_pop_single_element():
        test_stack = LinkedStack()
        test_stack.push("A")
        A_node = test_stack._header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None
        assert len(test_stack) == 1
        assert test_stack.pop() == "A"
        assert len(test_stack) == 0
        assert test_stack._header._next is None

    @staticmethod
    def test_pop_multiple_elements():
        test_stack = LinkedStack()
        test_stack.push("A")
        test_stack.push("B")
        B_node = test_stack._header._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        A_node = B_node._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None
        assert len(test_stack) == 2
        assert "B" == test_stack.pop()
        assert test_stack._header._next == A_node
        assert A_node._next is None
        assert B_node._next is None
        assert len(test_stack) == 1
        assert "A" == test_stack.pop()
        assert test_stack._header._next is None
        assert A_node._next is None
        assert len(test_stack) == 0


class TestTop:
    """
    Tests for the 'top()' method of the LinkedStack class.
    """

    @staticmethod
    def test_top_empty():
        test_stack = LinkedStack()
        with pytest.raises(Exception):
            test_stack.top()

    @staticmethod
    def test_top_non_empty():
        test_stack = LinkedStack()
        test_stack.push("A")
        assert len(test_stack) == 1
        assert test_stack.top() == "A"
        assert len(test_stack) == 1
        assert test_stack.top() == "A"


class TestIsEmpty:
    """
    Tests for the 'is_empty()' method of the LinkedStack class.
    """

    @staticmethod
    def test_is_empty_empty():
        test_stack = LinkedStack()
        assert test_stack.is_empty() is True

    @staticmethod
    def test_is_empty_non_empty():
        test_stack = LinkedStack()
        test_stack.push("A")
        assert test_stack.is_empty() is False

    @staticmethod
    def test_is_empty_changing():
        test_stack = LinkedStack()
        assert test_stack.is_empty() is True
        test_stack.push("A")
        assert test_stack.is_empty() is False
        test_stack.pop()
        assert test_stack.is_empty() is True


class TestLen:
    """
    Tests for the __len__() method of the LinkedStack class.
    """

    @staticmethod
    def test_len():
        test_stack = LinkedStack()
        for i in range(10):
            assert len(test_stack) == i
            test_stack.push(i)
        for i in range(10):
            assert 10 - i == len(test_stack)
            test_stack.pop()



class TestGeneral:
    """Test a sequence of push and pop operations."""
    @staticmethod
    def test_random_ops():
        stack = LinkedStack()
        elems = [i for i in range(100)]
        for elem in elems:
            stack.push(elem)
            assert len(stack) == elem + 1
            assert stack.top() == elem
        for elem in reversed(elems):
            assert stack.pop() == elem
            assert len(stack) == elem
        assert stack.is_empty()