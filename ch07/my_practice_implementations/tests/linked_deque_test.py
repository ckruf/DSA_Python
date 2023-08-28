import pytest
from ch07.my_practice_implementations.linked_deque import _Node, LinkedDeque


class TestInsertFirst:
    """
    Tests for the 'insert_first()' method of the LinkedDeque class.
    """

    @staticmethod
    def test_insert_first():
        deque = LinkedDeque()
        deque.insert_first("A")
        A_node = deque._header._next
        assert deque._trailer._prev == A_node
        assert A_node._next == deque._trailer
        assert A_node._prev == deque._header

        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        assert deque.first() == "A"

        assert len(deque) == deque._size == 1

        deque.insert_first("B")
        assert len(deque) == deque._size == 2
        B_node = deque._header._next
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        assert deque.first() == "B"

        assert B_node._next == A_node
        assert B_node._prev == deque._header
        assert A_node._prev == B_node

        deque.insert_first("C")
        assert len(deque) == deque._size == 3
        C_node = deque._header._next
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"
        assert deque.first() == "C"

        assert B_node._prev == C_node
        assert C_node._next == B_node
        assert C_node._prev == deque._header


class TestInsertLast:
    """
    Tests for the 'insert_last()' method of the LinkedDeque class.
    """

    @staticmethod
    def test_insert_last():
        deque = LinkedDeque()
        deque.insert_last("A")
        A_node = deque._trailer._prev
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        assert deque.last() == "A"
        assert deque._header._next == A_node
        assert A_node._prev == deque._header
        assert A_node._next == deque._trailer
        assert len(deque) == deque._size == 1

        deque.insert_last("B")
        B_node = deque._trailer._prev
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        assert deque.last() == "B"
        assert A_node._next == B_node
        assert B_node._next == deque._trailer
        assert B_node._prev == A_node
        assert len(deque) == deque._size == 2

        deque.insert_last("C")
        C_node = deque._trailer._prev
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"
        assert deque.last() == "C"
        B_node._next == C_node
        assert C_node._next == deque._trailer
        assert C_node._prev == B_node
        assert len(deque) == deque._size == 3


class TestFirst:
    """
    Tests for the 'first()' method of the LinkedDeque class.
    """

    @staticmethod
    def test_first_when_empty():
        deque = LinkedDeque()
        with pytest.raises(Exception):
            deque.first()

    @staticmethod
    def test_first():
        deque = LinkedDeque()
        deque.insert_first("A")
        assert deque.first() == "A"
        deque.insert_first("B")
        assert deque.first() == "B"


class TestLast:
    """
    Tests for the 'last()' method of the LinkedDeque class.
    """

    @staticmethod
    def test_last_when_empty():
        deque = LinkedDeque()
        with pytest.raises(Exception):
            deque.last()

    @staticmethod
    def test_last():
        deque = LinkedDeque()
        deque.insert_last("A")
        assert deque.last() == "A"
        deque.insert_last("B")
        assert deque.last() == "B"


class TestDeleteFirst:
    """
    Tests for the 'delete_first()' method of the LinkedDeque class.
    """

    @staticmethod
    def test_delete_first_empty():
        deque = LinkedDeque()
        with pytest.raises(Exception):
            deque.delete_first()

    @staticmethod
    def test_delete_first():
        deque = LinkedDeque()
        # insert 3 test nodes and ensure they are actually the nodes we want
        deque.insert_last("A")
        A_node = deque._trailer._prev
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        deque.insert_last("B")
        B_node = deque._trailer._prev
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        deque.insert_last("C")
        C_node = deque._trailer._prev
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"

        # delete from front and make assertions
        assert len(deque) == deque._size == 3
        assert deque._header._next == A_node
        assert B_node._prev == A_node

        assert deque.delete_first() == "A"
        assert len(deque) == deque._size == 2
        assert deque._header._next == B_node
        assert B_node._prev == deque._header

        assert deque.delete_first() == "B"
        assert len(deque) == deque._size == 1
        assert deque._header._next == C_node
        assert C_node._prev == deque._header

        assert deque.delete_first() == "C"
        assert len(deque) == deque._size == 0
        assert deque._header._next == deque._trailer
        assert deque._trailer._prev == deque._header


class TestDeleteLast:
    """
    Tests for the 'delete_last()' method of the LinkedDeque class.
    """

    @staticmethod
    def test_delete_last_empty():
        deque = LinkedDeque()
        with pytest.raises(Exception):
            deque.delete_last()

    @staticmethod
    def test_delete_last():
        deque = LinkedDeque()
        deque.insert_last("A")
        A_node = deque._trailer._prev
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        deque.insert_last("B")
        B_node = deque._trailer._prev
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        deque.insert_last("C")
        C_node = deque._trailer._prev
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"

        assert len(deque) == deque._size == 3
        assert B_node._next == C_node
        assert deque._trailer._prev == C_node

        assert deque.delete_last() == "C"
        assert len(deque) == deque._size == 2
        assert deque._trailer._prev == B_node
        assert B_node._next == deque._trailer

        assert deque.delete_last() == "B"
        assert len(deque) == deque._size == 1
        assert deque._trailer._prev == A_node
        assert A_node._next == deque._trailer

        assert deque.delete_last() == "A"
        assert len(deque) == deque._size == 0
        assert deque._trailer._prev == deque._header
        assert deque._header._next == deque._trailer


class TestGeneral:
    """
    Test a series of insert and delete operations
    """

    @staticmethod
    def test_general():
        deque = LinkedDeque()
        count = 0
        for i in range(10, 0, -1):
            deque.insert_last(i)
            assert deque.last() == i
            assert len(deque) == count + 1
            count += 1
        for i in range(9, 0, -1):
            deque.insert_first(i)
            assert deque.first() == i
            assert len(deque) == count + 1
            count += 1

        for i in range(1, 10):
            assert deque.last() == i
            assert deque.first() == i
            assert deque.delete_first() == i
            assert deque.delete_last() == i
            assert len(deque) == count - (2 * i)

        assert len(deque) == 1
        assert deque.first() == deque.last() == 10
