"""This file contains tests for exercise 7.25"""
import pytest
from ch07.exercises.linked_queue_25 import LinkedQueue, Node


class TestEnqueue:
    """Tests for the 'enqueue()' method of the LinkedQueue class."""

    @staticmethod
    def test_enqueue_empty():
        test_q = LinkedQueue()
        assert len(test_q) == 0
        assert isinstance(test_q._header, Node)
        assert test_q._header._element is None
        assert test_q._header == test_q._tail
        test_q.enqueue("A")
        assert len(test_q) == 1
        A_node = test_q._header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None
        assert test_q._tail == A_node

    @staticmethod
    def test_enqueue_non_empty():
        test_q = LinkedQueue()
        test_q.enqueue("A")
        assert len(test_q) == 1
        A_node = test_q._header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next is None
        assert test_q._tail == A_node
        test_q.enqueue("B")
        B_node = A_node._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next is None
        assert len(test_q) == 2
        assert test_q._tail == B_node


class TestDequeue:
    """Tests for the 'dequeue()' method of the LinkedQueue class."""

    @staticmethod
    def test_dequeue_empty():
        test_q = LinkedQueue()
        with pytest.raises(Exception):
            test_q.dequeue()

    @staticmethod
    def test_dequeue_single():
        test_q = LinkedQueue()
        test_q.enqueue("A")
        assert len(test_q) == 1
        A_node = test_q._header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert test_q._tail == A_node

        assert test_q.dequeue() == "A"
        assert test_q._header._next is None
        assert test_q._tail == test_q._header
        assert len(test_q) == 0

    @staticmethod
    def test_dequeue_multiple():
        test_q = LinkedQueue()
        test_q.enqueue("A")
        test_q.enqueue("B")
        assert len(test_q) == 2
        A_node = test_q._header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        B_node = A_node._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next is None
        assert test_q._tail == B_node

        assert test_q.dequeue() == "A"
        assert len(test_q) == 1
        assert test_q._header._next == B_node
        assert test_q._tail == B_node
        assert B_node._next is None
        assert A_node._next is None

        assert test_q.dequeue() == "B"
        assert len(test_q) == 0
        assert test_q._header._next is None
        assert test_q._header == test_q._tail


class TestFirst:
    """Tests for the 'first()' method of the LinkedQueue class."""

    @staticmethod
    def test_first_empty():
        test_q = LinkedQueue()
        with pytest.raises(Exception):
            test_q.first()

    @staticmethod
    def test_first_non_empty():
        test_q = LinkedQueue()
        test_q.enqueue("A")
        assert test_q.first() == "A"
        test_q.enqueue("B")
        assert test_q.first() == "A"
        test_q.dequeue()
        assert test_q.first() == "B"


class TestIsEmpty:
    """Tests for the 'is_empty()' method of the LinkedQueue class."""

    @staticmethod
    def test_is_empty_empty():
        test_q = LinkedQueue()
        assert test_q.is_empty() is True

    @staticmethod
    def test_is_empty_non_empty():
        test_q = LinkedQueue()
        test_q.enqueue("A")
        assert test_q.is_empty() is False


class TestLen:
    """Tests for the '__len__()' method of the LinkedQueue class."""

    @staticmethod
    def test_len():
        test_q = LinkedQueue()
        for i in range(5):
            assert len(test_q) == i
            test_q.enqueue(i)


class TestGeneral:
    """Test a series of enqueue and dequeue operations"""

    @staticmethod
    def test_general():
        test_q = LinkedQueue()
        for i in range(10):
            assert len(test_q) == i
            test_q.enqueue(i)
            assert test_q.first() == 0

        for i in range(10):
            assert test_q.first() == i
            assert test_q.dequeue() == i
            assert len(test_q) == 10 - (i + 1)

        assert len(test_q) == 0
        assert test_q.is_empty() is True

        # run same thing again to check if completely emptying and then
        # filling again is properly implemented

        for i in range(10):
            assert len(test_q) == i
            test_q.enqueue(i)
            assert test_q.first() == 0

        for i in range(10):
            assert test_q.first() == i
            assert test_q.dequeue() == i
            assert len(test_q) == 10 - (i + 1)

        assert len(test_q) == 0
        assert test_q.is_empty() is True
