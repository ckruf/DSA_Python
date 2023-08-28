"""File containg unit tests for exercise 7.32"""
import pytest
from ch07.exercises.circular_positional_list_32 import (
    CircularPositionalList,
    Node,
    Position,
)


class TestAddAfter:
    """
    Tests for the 'add_after()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_add_after_empty():
        test_list = CircularPositionalList()
        assert len(test_list) == 0
        assert test_list._cursor is None

        test_list.add_after("A")

        assert len(test_list) == 1
        A_node = test_list._cursor
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node
        assert A_node._prev == A_node

    @staticmethod
    def test_add_after_single_element():
        test_list = CircularPositionalList()
        test_list.add_after("A")
        assert len(test_list) == 1
        A_node = test_list._cursor
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node
        assert A_node._next == A_node

        test_list.add_after("B")

        assert len(test_list) == 2
        B_node = test_list._cursor
        assert isinstance(B_node, Node)
        assert B_node._next == A_node
        assert B_node._prev == A_node
        assert B_node._element == "B"
        assert A_node._next == B_node
        assert A_node._prev == B_node

    @staticmethod
    def test_add_after_multiple_elements():
        test_list = CircularPositionalList()
        test_list.add_after("A")
        test_list.add_after("B")
        assert len(test_list) == 2
        B_node = test_list._cursor
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == B_node._prev
        A_node = B_node._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node._prev == B_node

        test_list.add_after("C")

        assert len(test_list) == 3
        C_node = test_list._cursor
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        # changed/updated pointers
        assert C_node._next == A_node
        assert C_node._prev == B_node
        assert B_node._next == C_node
        assert A_node._prev == C_node

        # existing unchanged pointers
        assert A_node._next == B_node
        assert B_node._prev == A_node

        test_list.add_after("D")

        assert len(test_list) == 4
        D_node = test_list._cursor
        assert isinstance(D_node, Node)
        assert D_node._element == "D"

        assert D_node._next == A_node
        assert D_node._prev == C_node
        assert C_node._next == D_node
        assert A_node._prev == D_node


class TestAddBefore:
    """
    Tests for the 'add_before()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_add_before_empty():
        test_list = CircularPositionalList()
        assert len(test_list) == 0
        assert test_list._cursor is None

        test_list.add_before("A")

        assert len(test_list) == 1
        A_node = test_list._cursor
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node
        assert A_node._prev == A_node

    @staticmethod
    def test_add_before_single_element():
        test_list = CircularPositionalList()
        test_list.add_before("A")
        assert len(test_list) == 1
        A_node = test_list._cursor
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._prev == A_node
        assert A_node._next == A_node

        test_list.add_before("B")

        assert len(test_list) == 2
        B_node = test_list._cursor
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == A_node
        assert B_node._prev == A_node
        assert A_node._next == B_node
        assert A_node._prev == B_node

    @staticmethod
    def test_add_before_multiple_elements():
        test_list = CircularPositionalList()
        test_list.add_before("A")
        test_list.add_before("B")
        assert len(test_list) == 2
        B_node = test_list._cursor
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == B_node._prev
        A_node = B_node._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node._prev == B_node

        test_list.add_before("C")

        assert len(test_list) == 3
        C_node = test_list._cursor
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        # changed / updated pointers
        assert C_node._next == B_node
        assert C_node._prev == A_node
        assert B_node._prev == C_node
        assert A_node._next == C_node

        # existing unchanged pointers
        assert B_node._next == A_node
        assert A_node._prev == B_node

        test_list.add_before("D")

        assert len(test_list) == 4
        D_node = test_list._cursor
        assert isinstance(D_node, Node)

        assert D_node._element == "D"
        assert D_node._next == C_node
        assert D_node._prev == A_node
        assert A_node._next == D_node
        assert C_node._prev == D_node


class TestCurrentElement:
    """
    Tests for the 'current_element()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_current_element_empty():
        test_list = CircularPositionalList()
        assert test_list.current_element() is None

    @staticmethod
    def test_current_element_non_empty():
        test_list = CircularPositionalList()
        test_list.add_after("A")
        A_pos = test_list.current_element()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"


class TestMoveNext:
    """
    Tests for the 'move_next()' method of the CiruclarPostionalList class.
    """

    @staticmethod
    def test_move_next_empty():
        test_list = CircularPositionalList()
        with pytest.raises(Exception):
            test_list.move_next()

    @staticmethod
    def test_move_next_non_empty():
        test_list = CircularPositionalList()
        for e in "A", "B", "C":
            test_list.add_after(e)
        C_pos = test_list.current_element()
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"
        test_list.move_next()
        A_pos = test_list.current_element()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        test_list.move_next()
        B_pos = test_list.current_element()
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        test_list.move_next()
        C_pos_again = test_list.current_element()
        assert C_pos_again == C_pos


class TestMovePrevious:
    """
    Tests for the 'move_previous()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_move_previous_empty():
        test_list = CircularPositionalList()
        with pytest.raises(Exception):
            test_list.move_previous()

    @staticmethod
    def test_move_previous_non_empty():
        test_list = CircularPositionalList()
        for e in "A", "B", "C":
            test_list.add_after(e)
        C_pos = test_list.current_element()
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"
        test_list.move_previous()
        B_pos = test_list.current_element()
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        test_list.move_previous()
        A_pos = test_list.current_element()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        test_list.move_previous()
        assert test_list.current_element() == C_pos


class TestNextElement:
    """
    Tests for the 'next_element()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_next_element_empty():
        test_list = CircularPositionalList()
        with pytest.raises(Exception):
            test_list.next_element()

    @staticmethod
    def test_next_element_non_empty_no_argument():
        test_list = CircularPositionalList()
        test_list.add_after("A")
        A_pos = test_list.next_element()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        test_list.add_after("B")
        B_pos = test_list.current_element()
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        assert test_list.next_element() == A_pos
        test_list.move_next()
        assert test_list.current_element() == A_pos
        assert test_list.next_element() == B_pos

    @staticmethod
    def test_next_element_non_empty_argument_given():
        test_list = CircularPositionalList()
        for e in "A", "B", "C":
            test_list.add_after(e)
        C_pos = test_list.current_element()
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"
        A_pos = test_list.next_element()
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        B_pos = test_list.next_element(A_pos)
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        assert test_list.next_element(B_pos) == C_pos
        assert test_list.next_element(C_pos) == A_pos


class TestPreviousElement:
    """
    Tests for the 'previous_element()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_previous_element_empty():
        test_list = CircularPositionalList()
        with pytest.raises(Exception):
            test_list.previous_element()

    @staticmethod
    def test_previous_element_non_empty_no_argument():
        test_list = CircularPositionalList()
        for e in "A", "B", "C":
            test_list.add_after(e)
        C_pos = test_list.current_element()
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"
        B_pos = test_list.previous_element()
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"

    @staticmethod
    def test_previous_element_non_empty_argument_given():
        test_list = CircularPositionalList()
        for e in "A", "B", "C":
            test_list.add_after(e)
        C_pos = test_list.current_element()
        assert isinstance(C_pos, Position)
        assert C_pos.element() == "C"
        B_pos = test_list.previous_element(C_pos)
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        A_pos = test_list.previous_element(B_pos)
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        assert test_list.previous_element(A_pos) == C_pos


class TestDelete:
    """
    Tests for the 'delete()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_delete_empty():
        test_list = CircularPositionalList()
        with pytest.raises(Exception):
            test_list.delete()

    @staticmethod
    def test_delete_single_element():
        test_list = CircularPositionalList()
        test_list.add_after("A")
        assert len(test_list) == 1
        A_node = test_list._cursor
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node
        assert A_node._prev == A_node

        assert test_list.delete() == "A"

        assert len(test_list) == 0
        assert test_list._cursor is None
        assert A_node._next == A_node._prev == A_node._element == None

    @staticmethod
    def test_delete_multiple_elements():
        test_list = CircularPositionalList()
        for e in "A", "B", "C", "D":
            test_list.add_after(e)

        assert len(test_list) == 4

        # grab references to all nodes
        D_node = test_list._cursor
        assert isinstance(D_node, Node)
        assert D_node._element == "D"

        A_node = D_node._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        B_node = A_node._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        C_node = B_node._next
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        # make assertions about nodes/pointers which are going to change
        # after deletion
        assert C_node._next == D_node
        assert A_node._prev == D_node

        assert test_list.delete() == "D"

        assert len(test_list) == 3
        # check that cursor has advanced
        assert test_list._cursor == A_node
        # check preceding and following pointers have updated
        assert C_node._next == A_node
        assert A_node._prev == C_node
        # check garbage collection
        assert D_node._next == D_node._prev == D_node._element == None

        # make assertions about pointers which are going to change after deletion
        assert C_node._next == A_node
        assert B_node._prev == A_node

        assert test_list.delete() == "A"

        assert len(test_list) == 2
        # check that cursor has advanced
        assert test_list._cursor == B_node
        # check that preceding and following pointers have updated
        assert C_node._next == B_node
        assert B_node._prev == C_node
        # check garbage collection
        assert A_node._next == A_node._prev == A_node._element == None

        # make assertions about pointers which are going to change
        assert C_node._next == B_node
        assert C_node._prev == B_node

        assert test_list.delete() == "B"

        assert len(test_list) == 1
        # check that cursor has advanced
        assert test_list._cursor == C_node
        # check that preceding and following pointers have updated
        assert C_node._next == C_node
        assert C_node._prev == C_node
        # check garbage colleciton
        assert B_node._next == B_node._prev == B_node._element == None

        assert test_list.delete() == "C"
        assert len(test_list) == 0
        assert test_list.is_empty() is True
        assert test_list._cursor is None
        assert C_node._next == C_node._prev == C_node._element == None


class TestReplace:
    """
    Tests for the 'replace()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_replace_empty():
        test_list = CircularPositionalList()
        with pytest.raises(Exception):
            test_list.replace("A")

    @staticmethod
    def test_replace_non_empty():
        test_list = CircularPositionalList()
        test_list.add_after("A")
        pos = test_list.current_element()
        assert pos.element() == "A"
        test_list.replace("B")
        assert pos.element() == "B"


class TestIsEmpty:
    """
    Tests for the 'is_empty()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_is_empty_empty():
        test_list = CircularPositionalList()
        assert test_list.is_empty() is True

    @staticmethod
    def test_is_empty_not_empty():
        test_list = CircularPositionalList()
        test_list.add_after("A")
        assert test_list.is_empty() is False


class TestIter:
    """
    Tests for the '__iter__()' method of the CircularPositionalList class.
    """

    @staticmethod
    def test_iter_empty():
        test_list = CircularPositionalList()
        for _ in test_list:
            assert False

    @staticmethod
    def test_iter_single_element():
        test_list = CircularPositionalList()
        test_list.add_after("A")
        assert [e for e in test_list] == [
            "A",
        ]

    @staticmethod
    def test_iter_multiple_elements():
        test_list = CircularPositionalList()
        for e in "A", "B", "C":
            test_list.add_after(e)
        assert [e for e in test_list] == ["C", "A", "B"]
