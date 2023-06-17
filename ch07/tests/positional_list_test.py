"""
Tests for the Position class and the PositionalList class.
NOTE: These tests are dependent on a correct implementation of the
DoublyLinkedBase class.
"""
import pytest
from ch07.my_practice_implementations.positional_list import (
    PositionalList,
    Position,
    _Node,
)


class TestPosition:
    """
    Tests for the Position class.
    """

    @staticmethod
    def test_initialization():
        """
        Test that Position instance can be created.
        """
        test_list = PositionalList()
        test_node = _Node("A")
        test_pos = Position(test_list, test_node)

    @staticmethod
    def test_element():
        """
        Test the element() method.
        """
        test_list = PositionalList()
        test_element = "A"
        test_node = _Node(test_element)
        test_pos = Position(test_list, test_node)
        assert test_pos.element() == test_element

    @staticmethod
    def test_equality_equal():
        """
        Test the __eq__ method when Positions are equal.
        """
        test_list = PositionalList()
        test_element = "A"
        test_node = _Node(test_element)
        first_test_pos = Position(test_list, test_node)
        second_test_pos = Position(test_list, test_node)
        assert first_test_pos == second_test_pos

    @staticmethod
    def test_equality_different_type():
        """
        Test the __eq__ method when the object we are comparing the given
        position to is not a Position instance.
        """
        test_list = PositionalList()
        test_element = "A"
        test_node = _Node(test_element)
        test_pos = Position(test_list, test_node)
        assert (test_pos == 5) is False

    @staticmethod
    def test_equality_different_node():
        """
        Test the __eq__ method when the object we are comparing the given
        position to is a Position instance, but the node is different.
        """
        test_list = PositionalList()
        test_element = "A"
        first_test_node = _Node(test_element)
        second_test_node = _Node(test_element)
        # note that even though the Nodes both have the same element, and the
        # positions both belong to the same list, the Nodes are not equal,
        # because Python by default considers equality to be reference to the
        # same objects in memory, which these two nodes are not
        first_test_pos = Position(test_list, first_test_node)
        second_test_pos = Position(test_list, second_test_node)
        assert (first_test_pos == second_test_pos) is False

    @staticmethod
    def test_inequality_equal_nodes():
        """
        Test that the __ne__ method is implemented by checking inequality
        of equal Positions.
        """
        test_list = PositionalList()
        test_element = "A"
        test_node = _Node(test_element)
        first_test_pos = Position(test_list, test_node)
        second_test_pos = Position(test_list, test_node)
        assert (first_test_pos != second_test_pos) is False


class TestInsertBetween:
    """
    Test the '_insert_between()' method of the PositionalList class.
    This will only have a single test checking that the method returns
    a Position instance, because that is the only change to this overridden
    method compared to the base method. All other functionality is tested
    separately in the tests of the base method in the _DoublyLinkedBase class.
    """
    @staticmethod
    def test_position_instance_returned():
        test_list = PositionalList()
        inserted_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        assert isinstance(inserted_pos, Position)


class TestFirst:
    """
    Tests for the 'first()' method of the PositionalList class.
    Note that the _insert_between method is used, so that the tests do not
    rely on the correct implementation of methods such as 'add_first' and
    other 'add_' methods.
    """

    @staticmethod
    def test_first_single_element():
        """
        Test that the first() method works when there is one element in the
        list.
        """
        test_list = PositionalList()
        inserted_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        assert test_list.first() == inserted_pos

    @staticmethod
    def test_first_change_after_insertion():
        """
        Test that the first() method works both when an element is inserted
        in first position, and then after another element is inserted
        in the first position (ie first() changes).
        """
        test_list = PositionalList()
        first_pos = test_list._insert_between(
            "B", test_list._header, test_list._trailer
        )
        assert test_list.first() == first_pos
        new_first_pos = test_list._insert_between(
            "A", test_list._header, test_list._header._next
        )
        assert test_list.first() == new_first_pos

    @staticmethod
    def test_first_no_change_after_insertion():
        """
        Test that the first() method works both when an element is inserted
        in first position, and then after another element is inserted in
        the second position (ie first() shouldn't change).
        """
        test_list = PositionalList()
        first_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )

    @staticmethod
    def test_first_empty():
        """
        Test that the first() method works as expected when the PositionalList
        is empty. In this case, ValueError should be raised.
        """
        test_list = PositionalList()
        with pytest.raises(ValueError) as e_info:
            test_list.first()


class TestLast:
    """
    Tests for the 'last()' method of the PositionalList class.
    Note that the _insert_between method is used, so that the tests do not
    rely on the correct implementation of methods such as 'add_last' and
    other 'add_' methods.
    """

    @staticmethod
    def test_last_single_element():
        """
        Test that the last() method works when there is one element in the list.
        """
        test_list = PositionalList()
        inserted_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        assert test_list.last() == inserted_pos

    @staticmethod
    def test_last_change_after_insertion():
        """
                Test that the last() method works both when an element is inserted
        into an initially empty list, and then after another element is
        added into the last position (ie last() changes).
        """
        test_list = PositionalList()
        inserted_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        assert test_list.last() == inserted_pos
        new_last_pos = test_list._insert_between(
            "B", inserted_pos._node, test_list._trailer
        )
        assert test_list.last() == new_last_pos

    @staticmethod
    def test_last_no_change_after_insertion():
        """
        Test that the last() method works both when an element is inserted
        into an initially empty list, and then after another lement is added
        into the first position (ie last() should not change).
        """
        test_list = PositionalList()
        inserted_pos = test_list._insert_between(
            "B", test_list._header, test_list._trailer
        )
        assert test_list.last() == inserted_pos
        new_first_pos = test_list._insert_between(
            "A", test_list._header, inserted_pos._node
        )
        assert test_list.last() == inserted_pos

    @staticmethod
    def test_last_empty():
        """
        Test that the last() method works as expected when the PositionalList
        is Empty. In this case, ValueError should be raised.
        """
        test_list = PositionalList()
        with pytest.raises(ValueError) as e_info:
            test_list.last()


class TestBefore:
    """
    Tests for the 'before()' method of the PositionalList class.
    """
    
    @staticmethod
    def test_before_existing():
        """
        Test that the before() method returns the preceding Position when
        there is a preceding position.
        """
        test_list = PositionalList()
        first_position = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        second_position = test_list._insert_between(
            "B", first_position._node, test_list._trailer
        )
        assert test_list.before(second_position) == first_position
    
    @staticmethod
    def test_before_non_existing():
        """
        Test that the before() method returns None when there is no
        preceding position (ie calling before() on the first element).
        """
        test_list = PositionalList()
        first_position = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        assert test_list.before(first_position) is None


class TestAfter:
    """
    Tests for the 'after()' method of the PositionalList class.
    """

    @staticmethod
    def test_after_existing():
        """
        Test that the after() method returns the successing Position when
        there is a successing position.
        """
        test_list = PositionalList()
        first_position = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        second_position = test_list._insert_between(
            "B", first_position._node, test_list._trailer
        )
        assert test_list.after(first_position) == second_position

    @staticmethod
    def test_after_non_existing():
        """
        Test that the after() method returns None when there is no successing
        position (ie when calling after() on the last element).
        """
        test_list = PositionalList()
        first_position = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        assert test_list.after(first_position) is None


class TestIter:
    """
    Tests for the '__iter__()' dunder method of the PositionalList class,
    which enables iteration over a PositionalList. 
    """

    @staticmethod
    def test_iter_empty_list():
        """
        Test iterating over an empty PositionalList.
        """
        test_list = PositionalList()
        # if loop runs, test will fail
        for _ in test_list:
            assert False

    @staticmethod
    def test_iter_single_element_list():
        """
        Test iterating over a PositionalList with one element.
        """
        test_list = PositionalList()
        elements = ["A", ]
        test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        for expected, actual in zip(elements, test_list):
            assert expected == actual 

    @staticmethod
    def test_iter_multiple_element_list():
        """
        Test iterating over a PositionalList with mulitple elements.
        """
        test_list = PositionalList()
        elements = ["A", "B", "C"]
        first_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        second_pos = test_list._insert_between(
            "B", first_pos._node, test_list._trailer
        )
        test_list._insert_between(
            "C", second_pos._node, test_list._trailer
        )
        for expected, actual in zip(elements, test_list):
            assert expected == actual


class TestAddFirst:
    """
    Test the add_first() method of the PositionalList class.
    """

    @staticmethod
    def test_add_first_empty():
        """
        Test the add_first() method on an initially empty list.
        """
        test_list = PositionalList()
        first_pos = test_list.add_first("A")
        # check that what's returned by first() matches
        assert test_list.first() == first_pos
        # check that pointer on inserted node are correct
        assert first_pos._node._prev == test_list._header
        assert first_pos._node._next == test_list._trailer 
        # check that pointers on preceding and succeeding nodes updated
        assert test_list._header._next == first_pos._node
        assert test_list._trailer._prev == first_pos._node

    @staticmethod
    def test_add_first():
        """
        Test the add_first() method when the list is not empty.
        """
        test_list = PositionalList()
        B_pos = test_list.add_first("B")
        A_pos = test_list.add_first("A")
        # check that what's returned by first() matches
        assert test_list.first() == A_pos
        # check that pointer on inserted node are correct
        assert A_pos._node._prev == test_list._header
        assert A_pos._node._next == B_pos._node
        # check that pointers on preceding and succeeding nodes updated
        assert test_list._header._next == A_pos._node
        assert B_pos._node._prev == A_pos._node



