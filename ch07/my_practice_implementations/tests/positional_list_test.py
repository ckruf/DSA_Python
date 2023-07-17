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
        test_element = "A"
        first_pos = test_list.add_first(test_element)
        # test return value
        assert isinstance(first_pos, Position)
        assert first_pos.element() == test_element
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
        assert len(test_list) == 0
        B_pos = test_list.add_first("B")
        assert len(test_list) == 1
        A_pos = test_list.add_first("A")
        assert len(test_list) == 2
        # test return value
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        # check that what's returned by first() matches
        assert test_list.first() == A_pos
        # check that pointer on inserted node are correct
        assert A_pos._node._prev == test_list._header
        assert A_pos._node._next == B_pos._node
        # check that pointers on preceding and succeeding nodes updated
        assert test_list._header._next == A_pos._node
        assert B_pos._node._prev == A_pos._node


class TestAddLast:
    """
    Test the add_last() method of the PositionalList class.
    """

    @staticmethod
    def test_add_last_empty():
        """
        Test the add_last() method on an initially empty list.
        """
        test_list = PositionalList()
        test_element = "A"
        pos = test_list.add_last(test_element)
        # check return value
        assert isinstance(pos, Position)
        assert pos.element() == test_element
        # check that what's returned by last() matches
        assert test_list.last() == pos
        #check that pointers on inserted node are correct
        assert pos._node._prev == test_list._header
        assert pos._node._next == test_list._trailer
        # check that pointer on preceding and succeeding nodes updated
        assert test_list._header._next == pos._node
        assert test_list._trailer._prev == pos._node

    @staticmethod
    def test_add_last():
        """
        Test the add_last() method when the list is not empty.
        """
        test_list = PositionalList()
        assert len(test_list) == 0
        first_pos = test_list.add_last("A")
        assert len(test_list) == 1
        second_pos = test_list.add_last("B")
        assert len(test_list) == 2
        # check return value
        assert isinstance(second_pos, Position)
        assert second_pos.element() == "B"
        # check that what's returned by last() matches
        assert test_list.last() == second_pos
        # check that pointers on inserted node are correct
        assert second_pos._node._prev == first_pos._node
        assert second_pos._node._next == test_list._trailer
        # check that pointers on preceding and succeeding nodes updated
        assert first_pos._node._next == second_pos._node
        assert test_list._trailer._prev == second_pos._node

class TestAddBefore:
    """
    Test the add_before() method of the PositionalList class.
    """
    
    @staticmethod
    def test_add_before_first():
        """
        Test the add_before method when adding a node before the first node.
        """
        test_list = PositionalList()
        B_pos = test_list._insert_between(
            "B", test_list._header, test_list._trailer
        )
        A_pos = test_list.add_before(B_pos, "A")
        # check return value
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        # check what's returned by before() matches
        assert A_pos == test_list.before(B_pos)
        # check that pointers on inserted node are correct
        assert A_pos._node._next == B_pos._node
        assert A_pos._node._prev == test_list._header
        # check that pointers on preceding and succeeding nodes updated
        assert B_pos._node._prev == A_pos._node
        assert test_list._header._next == A_pos._node

    @staticmethod
    def test_add_before():
        """
        Test the add_before method when adding a node before any node (not
        the first node).
        """
        test_list = PositionalList()
        A_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        C_pos = test_list._insert_between(
            "C", A_pos._node, test_list._trailer
        )
        assert len(test_list) == 2
        B_pos = test_list.add_before(C_pos, "B")
        assert len(test_list) == 3
        # check return value
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        # check what's returned by before() matches
        assert test_list.before(C_pos) == B_pos
        # check that pointers on inserted node are correct
        assert B_pos._node._prev == A_pos._node
        assert B_pos._node._next == C_pos._node
        # check that pointers on preceding and succeeding nodes updated
        assert A_pos._node._next == B_pos._node
        assert C_pos._node._prev == B_pos._node


class TestAddAfter:
    """
    Test the add_after() method of the PositionalList class.
    """

    @staticmethod
    def test_add_after_last():
        """
        Test the add_after method when adding a node after the last node.
        """
        test_list = PositionalList()
        A_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        B_pos = test_list.add_after(A_pos, "B")
        # check return value
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        # check that what's returned by after() matches
        assert test_list.after(A_pos) == B_pos
        # check that pointers on inserted node are correct
        assert B_pos._node._prev == A_pos._node
        assert B_pos._node._next == test_list._trailer
        # check that pointers on preceding and succeeding nodes upated
        assert A_pos._node._next == B_pos._node
        assert test_list._trailer._prev == B_pos._node

    @staticmethod
    def test_add_after():
        """
        Test the add_after method when adding a node after any node node (not
        the last node).
        """
        test_list = PositionalList()
        A_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        C_pos = test_list._insert_between(
            "C", A_pos._node, test_list._trailer)
        assert len(test_list) == 2
        B_pos = test_list.add_after(A_pos, "B")
        assert len(test_list) == 3
        # check return value
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        # check that what's returned by 'after()' matches
        assert test_list.after(A_pos) == B_pos
        # check that pointers on inserted node are correct
        assert B_pos._node._prev == A_pos._node
        assert B_pos._node._next == C_pos._node
        # check that pointers on preceding and succeeding nodes updated
        assert A_pos._node._next == B_pos._node
        assert C_pos._node._prev == B_pos._node 


class TestDelete:
    """
    Test the 'delete()' method of the PositionalList class.
    """

    @staticmethod
    def test_delete():
        """
        One complete test of the delete method. 
        - Deletes a middle node
        - Checks return value of method
        - Checks that pointers of preceding and succeeding node updated
        - Checks that 'len' decremented
        """
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        B_pos = test_list.add_last("B")
        C_pos = test_list.add_last("C")
        # assertions about state before deleting
        assert len(test_list) == 3
        assert A_pos._node._next == B_pos._node
        assert C_pos._node._prev == B_pos._node

        deleted_element = test_list.delete(B_pos)
        assert deleted_element == "B"
        assert len(test_list) == 2
        assert A_pos._node._next == C_pos._node
        assert C_pos._node._prev == A_pos._node
        # assert node is 'discarded' by setting everything to None
        assert B_pos._node._prev is None
        assert B_pos._node._next is None
        assert B_pos._node._element is None


class TestReplace:
    """
    Test the 'replace'()' method of the PositionalList class.
    """

    @staticmethod
    def test_replace():
        """
        One complete test of the 'replace' method.
        """
        test_list = PositionalList()
        A_pos = test_list.add_last("A")
        second_pos = test_list.add_last(2)
        C_pos = test_list.add_last("C")

        assert len(test_list) == 3

        assert A_pos._node._next == second_pos._node
        assert C_pos._node._prev == second_pos._node

        assert second_pos._node._prev == A_pos._node
        assert second_pos._node._next == C_pos._node
        
        assert second_pos.element() == 2

        test_list.replace(second_pos, "B")

        # we are not replacing the whole node, but just the element of the node
        # so the pointers should stay the same
        assert A_pos._node._next == second_pos._node
        assert C_pos._node._prev == second_pos._node
        
        assert second_pos._node._prev == A_pos._node
        assert second_pos._node._next == C_pos._node
        assert len(test_list) == 3
        assert second_pos.element() == "B"


class TestValidate:
    """
    Test the '_validate()' method of the PositionalList class.
    This method is used in all PositionalList methods which take a Position
    instance as argument, in order to - surprisingly - validate that the
    Position is legit (is actually Position instance, actually belongs
    to this PositionalList, is not deprecated).
    """

    @staticmethod
    def test_fails_not_position_instance():
        """
        Test that the '_validate()' method raises TypeError when
        it is given an object which is not a Position instance.
        """
        test_list = PositionalList()
        with pytest.raises(TypeError) as e_info:
            test_list._validate(5)

    @staticmethod
    def test_fails_when_container_is_not_list():
        """
        Test that the '_validate()' method raises ValueError when it is given
        a Position instance whose _container is a different PositionalList.
        """
        test_list = PositionalList()
        different_list = PositionalList()
        test_node = _Node("B", _Node("A"), _Node("C"))
        test_pos = Position(different_list, test_node)
        with pytest.raises(ValueError) as e_info:
            test_list._validate(test_pos)

    @staticmethod
    def test_fails_when_next_is_none():
        """
        Test that the '_validate()' method raises ValueError when p._node._next
        is None. This is the check used to determine whether we are dealing
        with a deprecated node (for example one which has since been deleted
        from the list).s
        """
        test_list = PositionalList()
        test_node = _Node("A")
        test_pos = Position(test_list, test_node)
        with pytest.raises(ValueError) as e_info:
            test_list._validate(test_pos)


class TestGetNodeAtIndex:
    """
    Test the '_get_node_at_index()' method of the PositionalList class.
    """

    @staticmethod
    def test_get_node_at_index():
        test_list = PositionalList()
        for e in "A", "B", "C":
            test_list.add_last(e)
        
        A_node = test_list._header._next
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"

        B_node = A_node._next
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"

        C_node = B_node._next
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"

        assert test_list._get_node_at_index(0) == A_node
        assert test_list._get_node_at_index(1) == B_node
        assert test_list._get_node_at_index(2) == C_node


class TestMax:
    """
    Test the 'max()' method of the PositionalList class.
    """

    @staticmethod
    def test_max_empty():
        test_list = PositionalList()
        with pytest.raises(Exception):
            test_list.max()

    @staticmethod
    def test_max_single_element():
        test_list = PositionalList()
        test_list.add_last(10)
        assert test_list.max() == 10

    @staticmethod
    def test_max_multiple_elements():
        test_list = PositionalList()
        test_list.add_last(10)
        test_list.add_last(6)
        test_list.add_last(3)
        assert test_list.max() == 10
        test_list.add_first(15)
        assert test_list.max() == 15
        test_list.add_last(100)
        assert test_list.max() == 100


class TestFind:
    """
    Test the 'find()' method of the PositionalList class.
    """

    @staticmethod
    def test_find_non_existent_empty():
        test_list = PositionalList()
        assert test_list.find("A") is None

    @staticmethod
    def test_find_non_existent_full():
        test_list = PositionalList()
        for e in "A", "B", "C":
            test_list.add_last(e)
        assert test_list.find("D") is None

    @staticmethod
    def test_find_existing():
        test_list = PositionalList()
        for e in "A", "B", "C", "D":
            test_list.add_last(e)
        A_pos = test_list.first()
        B_pos = test_list.after(A_pos)
        C_pos = test_list.after(B_pos)
        D_pos = test_list.after(C_pos)
        assert test_list.find("A") == A_pos
        assert test_list.find("B") == B_pos
        assert test_list.find("C") == C_pos
        assert test_list.find("D") == D_pos


class TestFindRecursive:
    """
    Test the 'find_recursive()' method of the PositionalList class.
    """

    @staticmethod
    def test_find_non_existent_empty():
        test_list = PositionalList()
        assert test_list.find_recursive("A") is None

    @staticmethod
    def test_find_non_existent_full():
        test_list = PositionalList()
        for e in "A", "B", "C":
            test_list.add_last(e)
        assert test_list.find_recursive("D") is None

    @staticmethod
    def test_find_existing():
        test_list = PositionalList()
        for e in "A", "B", "C", "D":
            test_list.add_last(e)
        A_pos = test_list.first()
        B_pos = test_list.after(A_pos)
        C_pos = test_list.after(B_pos)
        D_pos = test_list.after(C_pos)
        assert test_list.find_recursive("A") == A_pos
        assert test_list.find_recursive("B") == B_pos
        assert test_list.find_recursive("C") == C_pos
        assert test_list.find_recursive("D") == D_pos


class TestReverse:
    """
    Test the '__reversed__()' method of the PositionalList class.
    """

    @staticmethod
    def test_reversed_empty():
        test_list = PositionalList()
        for e in reversed(test_list):
            assert False

    @staticmethod
    def test_reversed_full():
        test_list = PositionalList()
        elems = ["A", "B", "C", "D", "E"]
        for e in elems:
            test_list.add_last(e)
        assert [e for e in elems] == [e for e in test_list]
        assert [e for e in reversed(elems)] == [e for e in reversed(test_list)]



class TestAddBeforeComposite:
    """
    Tests for the 'add_before_composite()' method of the PositionalList class.
    """

    @staticmethod
    def test_add_before_first():
        """
        Test the add_before method when adding a node before the first node.
        """
        test_list = PositionalList()
        B_pos = test_list._insert_between(
            "B", test_list._header, test_list._trailer
        )
        A_pos = test_list.add_before_composite(B_pos, "A")
        # check return value
        assert isinstance(A_pos, Position)
        assert A_pos.element() == "A"
        # check what's returned by before() matches
        assert A_pos == test_list.before(B_pos)
        # check that pointers on inserted node are correct
        assert A_pos._node._next == B_pos._node
        assert A_pos._node._prev == test_list._header
        # check that pointers on preceding and succeeding nodes updated
        assert B_pos._node._prev == A_pos._node
        assert test_list._header._next == A_pos._node

    @staticmethod
    def test_add_before():
        """
        Test the add_before method when adding a node before any node (not
        the first node).
        """
        test_list = PositionalList()
        A_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
        C_pos = test_list._insert_between(
            "C", A_pos._node, test_list._trailer
        )
        assert len(test_list) == 2
        B_pos = test_list.add_before_composite(C_pos, "B")
        assert len(test_list) == 3
        # check return value
        assert isinstance(B_pos, Position)
        assert B_pos.element() == "B"
        # check what's returned by before() matches
        assert test_list.before(C_pos) == B_pos
        # check that pointers on inserted node are correct
        assert B_pos._node._prev == A_pos._node
        assert B_pos._node._next == C_pos._node
        # check that pointers on preceding and succeeding nodes updated
        assert A_pos._node._next == B_pos._node
        assert C_pos._node._prev == B_pos._node


class TestAddLastComposite:
    """
    Test the 'add_last_composite()' method of the PositionalList class.
    """

    @staticmethod
    def test_add_last_empty():
        """
        Test the add_last() method on an initially empty list.
        """
        test_list = PositionalList()
        test_element = "A"
        pos = test_list.add_last_composite(test_element)
        # check return value
        assert isinstance(pos, Position)
        assert pos.element() == test_element
        # check that what's returned by last() matches
        assert test_list.last() == pos
        #check that pointers on inserted node are correct
        assert pos._node._prev == test_list._header
        assert pos._node._next == test_list._trailer
        # check that pointer on preceding and succeeding nodes updated
        assert test_list._header._next == pos._node
        assert test_list._trailer._prev == pos._node

    @staticmethod
    def test_add_last():
        """
        Test the add_last() method when the list is not empty.
        """
        test_list = PositionalList()
        assert len(test_list) == 0
        first_pos = test_list.add_last_composite("A")
        assert len(test_list) == 1
        second_pos = test_list.add_last_composite("B")
        assert len(test_list) == 2
        # check return value
        assert isinstance(second_pos, Position)
        assert second_pos.element() == "B"
        # check that what's returned by last() matches
        assert test_list.last() == second_pos
        # check that pointers on inserted node are correct
        assert second_pos._node._prev == first_pos._node
        assert second_pos._node._next == test_list._trailer
        # check that pointers on preceding and succeeding nodes updated
        assert first_pos._node._next == second_pos._node
        assert test_list._trailer._prev == second_pos._node