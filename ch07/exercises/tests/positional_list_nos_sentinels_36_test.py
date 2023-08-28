"""File containing tests for exercise 7.36"""
from unittest.mock import MagicMock
from ch07.exercises.positional_list_no_sentinels_36 import (
    PositionalList,
    Position,
    Node,
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
        A_pos = test_list.add_first("A")
        assert len(test_list) == 1
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        A_node = A_pos._node
        assert isinstance(A_node, Node)
        assert A_node._next == A_node._prev == None

        assert "A" == test_list.delete_first()

        assert len(test_list) == 0
        assert test_list._first is None
        assert test_list._last is None
        assert A_node._element == A_node._next == A_node._prev == None

    @staticmethod
    def test_delete_first_two_elements():
        """
        Special case - when we delete the first element in a two-element
        list, then the remaining items needs to be set as test_list._first
        """
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        B_pos = test_list.add_last("B")
        assert len(test_list) == 2
        assert isinstance(A_pos, Position)
        assert isinstance(B_pos, Position)
        assert A_pos.element() == "A"
        assert B_pos.element() == "B"
        A_node = A_pos._node
        B_node = B_pos._node
        assert isinstance(A_node, Node)
        assert isinstance(B_node, Node)
        assert A_node._prev is None
        assert A_node._next == B_node
        assert B_node._prev == A_node
        assert B_node._next is None

        assert test_list.delete_first() == "A"

        assert len(test_list) == 1
        assert test_list._first == test_list._last == B_node
        assert B_node._prev == B_node._next == None
        # check garbage collection
        assert A_node._prev == A_node._next == A_node._element == None

    @staticmethod
    def test_delete_first():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        B_pos = test_list.add_last("B")
        C_pos = test_list.add_last("C")
        assert len(test_list) == 3
        assert isinstance(A_pos, Position)
        assert isinstance(B_pos, Position)
        assert isinstance(C_pos, Position)
        assert A_pos.element() == "A"
        assert B_pos.element() == "B"
        assert C_pos.element() == "C"
        A_node = A_pos._node
        B_node = B_pos._node
        C_node = C_pos._node
        assert isinstance(A_node, Node)
        assert isinstance(B_node, Node)
        assert isinstance(C_node, Node)
        assert A_node._prev is None
        assert A_node._next == B_node
        assert B_node._prev == A_node
        assert B_node._next == C_node
        assert C_node._prev == B_node
        assert C_node._next is None

        assert test_list.delete_first() == "A"

        assert len(test_list) == 2
        assert test_list._first == B_node
        assert test_list._last == C_node
        assert B_node._prev is None
        assert B_node._next == C_node
        assert C_node._prev == B_node
        assert C_node._next is None


class TestDeleteLast:
    """
    Tests for the 'delete_last()' method of the PositionalList class.
    """

    @staticmethod
    def test_delete_last_empty():
        test_list = PositionalList()
        with pytest.raises(Exception):
            test_list.delete_last()

    @staticmethod
    def test_delete_last_single_element():
        test_list = PositionalList()
        A_pos = test_list.add_first("A")
        assert len(test_list) == 1
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        A_node = A_pos._node
        assert isinstance(A_node, Node)
        assert A_node._next == A_node._prev == None

        assert "A" == test_list.delete_last()

        assert len(test_list) == 0
        assert test_list._first is None
        assert test_list._last is None
        assert A_node._element == A_node._next == A_node._prev == None

    @staticmethod
    def test_delete_last_two_elements():
        """
        Special case - when we delete the last element in a two-element
        list, then the remaining items needs to be set as test_list._last
        """
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        B_pos = test_list.add_last("B")
        assert len(test_list) == 2
        assert isinstance(A_pos, Position)
        assert isinstance(B_pos, Position)
        assert A_pos.element() == "A"
        assert B_pos.element() == "B"
        A_node = A_pos._node
        B_node = B_pos._node
        assert isinstance(A_node, Node)
        assert isinstance(B_node, Node)
        assert A_node._prev is None
        assert A_node._next == B_node
        assert B_node._prev == A_node
        assert B_node._next is None

        assert test_list.delete_last() == "B"

        assert len(test_list) == 1
        assert test_list._first == test_list._last == A_node
        assert A_node._prev == A_node._next == None
        # check garbage collection
        assert B_node._prev == B_node._next == B_node._element == None

    @staticmethod
    def test_delete_last():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        B_pos = test_list.add_last("B")
        C_pos = test_list.add_last("C")
        assert len(test_list) == 3
        assert isinstance(A_pos, Position)
        assert isinstance(B_pos, Position)
        assert isinstance(C_pos, Position)
        assert A_pos.element() == "A"
        assert B_pos.element() == "B"
        assert C_pos.element() == "C"
        A_node = A_pos._node
        B_node = B_pos._node
        C_node = C_pos._node
        assert isinstance(A_node, Node)
        assert isinstance(B_node, Node)
        assert isinstance(C_node, Node)
        assert A_node._prev is None
        assert A_node._next == B_node
        assert B_node._prev == A_node
        assert B_node._next == C_node
        assert C_node._prev == B_node
        assert C_node._next is None

        assert test_list.delete_last() == "C"

        assert len(test_list) == 2
        assert test_list._first == A_node
        assert test_list._last == B_node
        assert B_node._prev == A_node
        assert B_node._next is None
        # check garbage collection
        assert C_node._next == C_node._prev == C_node._element == None


class TestDelete:
    """
    Tests for the 'delete()' method of the PositionalList class.
    """

    @staticmethod
    def test_delete_only_element():
        """
        Test that '_delete_last_remainig_node()' is called when
        'delete()' is called on one-element list.
        """
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        test_list._delete_last_remaining_node = MagicMock()
        test_list.delete(A_pos)
        test_list._delete_last_remaining_node.assert_called_once()

    @staticmethod
    def test_delete_last():
        """
        Test that 'delete_last()' is called when 'delete()' is given the
        last element in the list.
        """
        test_list = PositionalList()
        test_list.add_last("A")
        B_pos = test_list.add_last("B")
        test_list.delete_last = MagicMock()
        test_list.delete(B_pos)
        test_list.delete_last.assert_called_once()

    @staticmethod
    def test_delete_first():
        """
        Test that 'delete_first()' is called when 'delete()' is given the
        first element in the list.
        """
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        test_list.add_last("B")
        test_list.delete_first = MagicMock()
        test_list.delete(A_pos)
        test_list.delete_first.assert_called_once()

    @staticmethod
    def test_delete():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        B_pos = test_list.add_last("B")
        C_pos = test_list.add_last("C")

        assert len(test_list) == 3

        A_node = A_pos._node
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        B_node = B_pos._node
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        C_node = C_pos._node
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        assert A_node._next == B_node
        assert B_node._prev == A_node
        assert B_node._next == C_node
        assert C_node._prev == B_node

        assert test_list.delete(B_pos) == "B"

        assert len(test_list) == 2
        assert A_node._next == C_node
        assert C_node._prev == A_node


class TestReplace:
    """Test for the 'replace()' method of the PositionalList class."""

    @staticmethod
    def test_replace():
        test_list = PositionalList()
        pos = test_list.add_last("A")
        assert pos.element() == "A"
        test_list.replace(pos, "B")
        assert pos.element() == "B"


class TestFirst:
    """Test for the 'first()' method of the PositionalList class."""

    @staticmethod
    def test_first():
        test_list = PositionalList()
        B_pos = test_list.add_last("B")
        assert test_list.first() == B_pos
        A_pos = test_list.add_first("A")
        assert test_list.first() == A_pos


class TestLast:
    """Test for the 'last()' method of the PositionalList class."""

    @staticmethod
    def test_last():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        assert test_list.last() == A_pos
        B_pos = test_list.add_last("B")
        assert test_list.last() == B_pos


class TestBefore:
    """
    Tests for the 'before()' method of the PositionalList class.
    """

    @staticmethod
    def test_before_first():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        assert test_list.before(A_pos) is None

    @staticmethod
    def test_before_not_first():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        B_pos = test_list.add_last("B")
        assert test_list.before(B_pos) == A_pos


class TestAfter:
    """
    Tests for the 'after()' method of the PositionalList class.
    """

    @staticmethod
    def test_after_last():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        assert test_list.after(A_pos) is None

    @staticmethod
    def test_after_not_last():
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        B_pos = test_list.add_last("B")
        assert test_list.after(A_pos) == B_pos


class TestIsEmpty:
    """
    Test the 'is_empty()' method of the PositionalList class.
    """

    @staticmethod
    def test_is_empty_empty():
        test_list = PositionalList()
        assert test_list.is_empty() is True

    @staticmethod
    def test_is_empty_not_empty():
        test_list = PositionalList()
        test_list.add_last("A")
        assert test_list.is_empty() is False


class TestIter:
    """
    Test the __iter__() method of the PositionalList class.
    """

    @staticmethod
    def test_iter_emtpy():
        test_list = PositionalList()
        assert [e for e in test_list] == []

    @staticmethod
    def test_iter_single_element():
        test_list = PositionalList()
        test_list.add_last("A")
        assert [e for e in test_list] == [
            "A",
        ]

    @staticmethod
    def test_iter_multiple_elements():
        test_list = PositionalList()
        elems = ["A", "B", "C"]
        for e in elems:
            test_list.add_last(e)
        assert [e for e in test_list] == elems
