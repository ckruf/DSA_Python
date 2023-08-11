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


class TestPop:
    """Tests for the 'pop()' method of the LeakyLinkedStack class."""

    @staticmethod
    def test_pop_empty():
        test_stack = LinkedLeakyStack()
        with pytest.raises(Exception):
            test_stack.pop()

    @staticmethod
    def test_pop_single_element():
        test_stack = LinkedLeakyStack()
        test_stack.push("A")
        assert isinstance(test_stack._top, Node)
        assert len(test_stack) == 1

        assert test_stack.pop() == "A"
        assert test_stack._top is None
        assert len(test_stack) == 0

    @staticmethod
    def test_pop_multiple_elements():
        test_stack = LinkedLeakyStack()
        for e in "A", "B", "C":
            test_stack.push(e)

        assert len(test_stack) == 3

        C_node = test_stack._top
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        B_node = C_node._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        A_node = B_node._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        assert test_stack.pop() == "C"
        assert len(test_stack) == 2
        assert test_stack._top == B_node
        assert C_node._next is None

        assert test_stack.pop() == "B"
        assert len(test_stack) == 1
        assert test_stack._top == A_node

        assert test_stack.pop() == "A"
        assert len(test_stack) == 0
        assert test_stack._top is None
        assert A_node._next is None


class TestTop:
    """Tests for the 'top()' method of the LeakyLinkedStack class."""

    @staticmethod
    def test_top_empty():
        test_stack = LinkedLeakyStack()
        with pytest.raises(Exception):
            test_stack.top()

    @staticmethod
    def test_top_non_empty():
        test_stack = LinkedLeakyStack()
        test_stack.push("A")
        assert len(test_stack) == 1
        assert test_stack.top() == "A"
        assert len(test_stack) == 1


class TestIsEmpty:
    """Tests for the 'is_empty()' method of the LeakyLinkedStack class."""

    @staticmethod
    def test_is_empty_empty():
        test_stack = LinkedLeakyStack()
        assert test_stack.is_empty() is True

    @staticmethod
    def test_is_empty_not_empty():
        test_stack = LinkedLeakyStack()
        test_stack.push("A")
        assert test_stack.is_empty() is False


class TestIter:
    """Tests for the '__iter__()' method of the LinkedLeakyStack class."""

    @staticmethod
    def test_iter_empty():
        test_stack = LinkedLeakyStack()
        for _ in test_stack:
            assert False

    @staticmethod
    def test_iter_single_element():
        test_stack = LinkedLeakyStack()
        test_stack.push("A")
        assert [
            "A",
        ] == [e for e in test_stack]

    @staticmethod
    def test_iter_mulitple_elements():
        test_stack = LinkedLeakyStack()
        elems = ["A", "B", "C"]
        for e in elems:
            test_stack.push(e)
        assert list(reversed(elems)) == [e for e in test_stack]


class TestStr:
    """Tests for the '__str__()' method of the LinkedLeakyStack class."""

    @staticmethod
    def test_str():
        test_stack = LinkedLeakyStack()
        assert str(test_stack) == str([])
        elems = ["A", "B", "C"]
        for e in elems:
            test_stack.push(e)
        assert str(list(reversed(elems))) == str(test_stack)
