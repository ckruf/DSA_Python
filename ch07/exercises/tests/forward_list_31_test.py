"""Tests for exercise 7.31"""
import pytest
from ch07.exercises.forward_list_31 import ForwardList, Node, Position


class TestAddFirst:
    """
    Tests for the 'add_first()' method of the ForwardList class.
    """

    @staticmethod
    def test_add_first_empty():
        test_list = ForwardList()
        assert len(test_list) == 0
        header = test_list._header
        assert header._next is None

        test_list.add_first("A")
        assert len(test_list) == 1
        A_node = header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

    @staticmethod
    def test_add_first_non_empty():
        test_list = ForwardList()
        assert len(test_list) == 0
        header = test_list._header
        assert header._next is None

        test_list.add_first("B")
        assert len(test_list) == 1
        B_node = header._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        test_list.add_first("A")
        assert len(test_list) == 2
        A_node = header._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node


class TestFirst:
    """
    Tests for the 'first()' method of the ForwardList class.
    """

    @staticmethod
    def test_first_empty():
        test_list = ForwardList()
        assert test_list.first() is None

    @staticmethod
    def test_first_non_empty():
        test_list = ForwardList()

        test_list.add_first("B")
        B_pos = test_list.first()
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"

        test_list.add_first("A")
        A_pos = test_list.first()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"


class TestAfter:
    """
    Tests for the 'after()' method of the ForwardList class.
    """

    @staticmethod
    def test_after_last():
        test_list = ForwardList()
        test_list.add_first("A")
        A_pos = test_list.first()
        assert test_list.after(A_pos) is None

    @staticmethod
    def test_after_not_last():
        test_list = ForwardList()
        test_list.add_first("B")
        B_pos = test_list.first()
        test_list.add_first("A")
        A_pos = test_list.first()
        assert test_list.after(A_pos) == B_pos


class TestIsEmpty:
    """
    Tests for the 'is_empty()' method of the ForwardList class.
    """

    @staticmethod
    def test_is_empty_empty():
        test_list = ForwardList()
        assert test_list.is_empty() is True

    @staticmethod
    def test_is_empty_not_empty():
        test_list = ForwardList()
        test_list.add_first("A")
        assert test_list.is_empty() is False


class TestIter:
    """
    Tests for the '__iter__()' method of the ForwardList class.
    """

    @staticmethod
    def test_iter_empty():
        test_list = ForwardList()
        assert [e for e in test_list] == []

    @staticmethod
    def test_iter_non_empty():
        test_list = ForwardList()
        for e in "C", "B", "A":
            test_list.add_first(e)
        assert [e for e in test_list] == ["A", "B", "C"]


class TestAddAfter:
    """
    Tests for the 'add_after()' method of the ForwardList class.
    """

    @staticmethod
    def test_add_after_last():
        test_list = ForwardList()
        test_list.add_first("A")
        A_pos = test_list.first()
        assert isinstance(A_pos, Position)
        assert test_list.after(A_pos) is None
        assert A_pos.element() == "A"
        assert len(test_list) == 1

        test_list.add_after(A_pos, "B")
        assert len(test_list) == 2
        B_pos = test_list.after(A_pos)
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"

    @staticmethod
    def test_add_after_middle():
        test_list = ForwardList()
        test_list.add_first("C")
        test_list.add_first("A")
        assert len(test_list) == 2
        A_pos = test_list.first()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        C_pos = test_list.after(A_pos)
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"

        test_list.add_after(A_pos, "B")
        assert len(test_list) == 3
        B_pos = test_list.after(A_pos)
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        assert test_list.after(B_pos) == C_pos


class TestReplace:
    """
    Test for the 'replace()' method of the ForwardList class.
    """

    @staticmethod
    def test_replace():
        test_list = ForwardList()
        test_list.add_first("A")
        pos = test_list.first()
        assert pos.element() == "A"
        test_list.replace(pos, "B")
        assert pos.element() == "B"


class TestDelete:
    """
    Tests for the 'delete()' method of the ForwardList class.
    """

    @staticmethod
    def test_delete_last():
        test_list = ForwardList()
        test_list.add_first("A")
        assert len(test_list) == 1
        A_pos = test_list.first()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        test_list.delete(A_pos)
        assert len(test_list) == 0
        assert test_list.first() is None

    @staticmethod
    def test_delete_not_last():
        test_list = ForwardList()
        for e in "C", "B", "A":
            test_list.add_first(e)
        assert len(test_list) == 3
        assert [e for e in test_list] == ["A", "B", "C"]
        A_pos = test_list.first()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        B_pos = test_list.after(A_pos)
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        C_pos = test_list.after(B_pos)
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"

        test_list.delete(B_pos)
        assert len(test_list) == 2
        assert test_list.after(A_pos) == C_pos
        assert [e for e in test_list] == ["A", "C"]

    @staticmethod
    def test_delete_not_in_list():
        test_list = ForwardList()
        for e in "C", "B", "A":
            test_list.add_first(e)
        fake_pos = Position(test_list, Node("D"))
        with pytest.raises(Exception):
            test_list.delete(fake_pos)
