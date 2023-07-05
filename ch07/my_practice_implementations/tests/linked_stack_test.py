"""
Tests for the LinkedStack class.
"""
import pytest
from ch07.my_practice_implementations.linked_stack import LinkedStack, _Node


class TestInit:
    """Test the __init__ method of the LinkedStack class"""

    @staticmethod
    def test_init():
        stack = LinkedStack()
        assert stack._head is None
        assert stack._size == 0


class TestPush:
    """Test the push() method of the LinkedStack class"""

    @staticmethod
    def test_push_initially_empty():
        """Test the 'push()' method on an initially empty stack."""
        stack = LinkedStack()
        stack.push("A")
        assert isinstance(stack._head, _Node)
        assert stack._head._element == "A"

    @staticmethod
    def test_push_populated():
        """
        Test the 'push()' method when the stack is not empty to begin with.
        """
        stack = LinkedStack()
        stack.push("B")
        stack.push("A")
        assert isinstance(stack._head, _Node)
        assert stack._head._element == "A"
        next_node = stack._head._next
        assert isinstance(next_node, _Node)
        assert next_node._element == "B"
        assert next_node._next is None

    @staticmethod
    def test_push_increments_size():
        """
        Test that _size and len() of the stack increments after 'push()'.
        """
        stack = LinkedStack()
        assert stack._size == 0
        assert len(stack) == 0
        stack.push("B")
        assert stack._size == 1
        assert len(stack) == 1
        stack.push("A")
        assert stack._size == 2
        assert len(stack) == 2


class TestPop:
    """Test the 'pop()' method of the LinkedStack class."""

    @staticmethod
    def test_pop_empty():
        """
        Test that the 'pop()' method raises an Exception when attempting 
        to pop from an empty stack.
        """
        stack = LinkedStack()
        with pytest.raises(Exception):
            stack.pop()

    @staticmethod
    def test_pop_single_reassigns_head():
        """
        Test that the 'pop()' method correctly sets new '_head' if the stack
        ends up empty after popping.
        """
        stack = LinkedStack()
        stack.push("A")
        stack.pop()
        assert stack._head is None


    @staticmethod
    def test_pop_populated_reassigns_head():
        """
        Test that the 'pop()' method correctly sets new '_head' 
        """
        stack = LinkedStack()
        stack.push("A")
        stack.push("B")
        stack.pop()
        assert isinstance(stack._head, _Node)
        assert stack._head._element == "A"

    @staticmethod
    def test_pop_return():
        """Test that the 'pop()' method returns the element"""
        stack = LinkedStack()
        stack.push("A")
        stack.push("B")
        assert stack.pop() == "B"
        assert stack.pop() == "A"

    @staticmethod
    def test_pop_decrements_size():
        """Test that _size and len() of the stack decrements after 'pop()'."""
        stack = LinkedStack()
        stack.push("A")
        stack.push("B")
        assert stack._size == 2
        assert len(stack) == 2
        stack.pop()
        assert stack._size == 1
        assert len(stack) == 1
        stack.pop()
        assert stack._size == 0
        assert len(stack) == 0


class TestTop:
    """Test the 'top()' method of the LinkedStack class"""
    
    @staticmethod
    def test_top_empty():
        """Test that 'top()' raises Exception when stack is empty"""
        stack = LinkedStack()
        with pytest.raises(Exception):
            stack.top()

    @staticmethod
    def test_top():
        stack = LinkedStack()
        stack.push("A")
        assert stack.top() == "A"
        stack.push("B")
        assert stack.top() == "B"
        stack.pop()
        assert stack.top() == "A"


class TestLen:
    """Test the __len__() method of the LinkedStack class"""

    @staticmethod
    def test_len_empty():
        stack = LinkedStack()
        assert len(stack) == 0

    @staticmethod
    def test_len():
        stack = LinkedStack()
        for i in range(10):
            stack.push(i)
            assert len(stack) == i + 1


class TestIsEmpty:
    """Test the 'is_empty()' method of the LinkedStack class"""

    @staticmethod
    def test_is_empty_empty():
        stack = LinkedStack()
        assert stack.is_empty() is True

    @staticmethod
    def test_is_empty_not_empty():
        stack = LinkedStack()
        stack.push("A")
        assert stack.is_empty() is False


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
