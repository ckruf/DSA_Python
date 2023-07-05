"""
Tests for the DoublyLinkedBase class.
"""
from ch07.my_practice_implementations.doubly_linked_list import _DoublyLinkedBase, _Node


class TestInit:
    """
    Test the __init__ method of the DoublyLinkedBase class.
    """

    @staticmethod
    def test_init():
        test_base = _DoublyLinkedBase()
        assert test_base._size == 0
        assert isinstance(test_base._header, _Node)
        assert isinstance(test_base._trailer, _Node)
        assert test_base._header._next == test_base._trailer
        assert test_base._trailer._prev == test_base._header


class TestLen:
    """
    Test the __len__ method of the DoublyLinkedBase class
    """

    @staticmethod
    def test_len_zero():
        test_base = _DoublyLinkedBase()
        assert len(test_base) == 0

    @staticmethod
    def test_len_non_zero():
        test_base = _DoublyLinkedBase()
        test_base._size = 10
        assert len(test_base) == 10


class TestIsEmpty:
    """
    Test the 'is_empty()' method of the DoublyLinkedBase class
    """

    @staticmethod
    def test_empty():
        test_base = _DoublyLinkedBase()
        assert test_base.is_empty() is True

    @staticmethod
    def test_non_empty():
        test_base = _DoublyLinkedBase()
        test_base._size = 10
        assert test_base.is_empty() is False

    
class TestInsertBetween:
    """
    Test the 'insert_between()' method of the _DoublyLinkedBase class.
    """

    @staticmethod
    def test_insert_between_complete():
        """
        Test the entire functionality of the _insert_between() method.
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        initial_length = len(test_base)
        new_node = test_base._insert_between(
            test_element, test_base._header, test_base._trailer
        )
        # test return value
        assert isinstance(new_node, _Node)
        assert new_node._element == test_element
        # test pointers on inserted node
        assert new_node._next == test_base._trailer
        assert new_node._prev == test_base._header
        ## test pointers on preceding and succeeding nodes
        assert test_base._header._next == new_node
        assert test_base._trailer._prev == new_node
        # test that length increased
        new_length = len(test_base)
        assert new_length == initial_length + 1

    @staticmethod
    def test_insert_between_return_value():
        """
        Test the return value of the _insert_between() method
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        new_node = test_base._insert_between(
            test_element, test_base._header, test_base._trailer
        )
        assert isinstance(new_node, _Node)
        assert new_node._element == test_element

    @staticmethod
    def test_insert_between_pointers_inserted_node():
        """
        Test that the pointers of the inserted node are correctly set. 
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        new_node = test_base._insert_between(
            test_element, test_base._header, test_base._trailer
        )
        assert new_node._next == test_base._trailer
        assert new_node._prev == test_base._header


    @staticmethod
    def test_insert_between_pointers_neighbours():
        """
        Test that the pointers of the neighbouring nodes of the inserted
        node are correctly set.
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        new_node = test_base._insert_between(
            test_element, test_base._header, test_base._trailer
        )
        assert test_base._header._next == new_node
        assert test_base._trailer._prev == new_node

    @staticmethod
    def test_insert_between_increments_length():
        """
        Test that the length of the _DoublyLinkedBase instance is incremented
        by one after insertion
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        initial_length = len(test_base)
        test_base._insert_between(
            test_element, test_base._header, test_base._trailer
        )
        new_length = len(test_base)
        assert new_length == initial_length + 1


class TestDeleteNode:
    """
    Test the '_delete_node()' method of the _DoublyLinkedBase class.
    """

    @staticmethod
    def test_delete_node_complete():
        """
        Test the entire functionality of the _delete_node() method.
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        # insert new node manually so test is not dependent
        # on _insert_between() method being correct
        new_node = _Node(test_element, test_base._header, test_base._trailer)
        test_base._header._next = new_node
        test_base._trailer._prev = new_node
        test_base._size += 1
        initial_length = len(test_base)
        returned_element = test_base._delete_node(new_node)
        # test pointers on neighbouring nodes
        assert test_base._header._next == test_base._trailer
        assert test_base._trailer._prev == test_base._header
        # test that size decreased
        new_length = len(test_base)
        assert initial_length == new_length + 1
        # test return value
        assert returned_element == test_element
        # test deleted node deprecation
        assert new_node._prev is None
        assert new_node._next is None
        assert new_node._element is None

    @staticmethod
    def test_delete_node_pointers_neighbours():
        """
        Test that '_delete_node()' correctly sets pointers on neighbouring
        nodes.
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        # insert new node manually so test is not dependent
        # on _insert_between() method being correct
        new_node = _Node(test_element, test_base._header, test_base._trailer)
        test_base._header._next = new_node
        test_base._trailer._prev = new_node
        test_base._delete_node(new_node)
        # test pointers on neighbouring nodes
        assert test_base._header._next == test_base._trailer
        assert test_base._trailer._prev == test_base._header

    @staticmethod
    def test_delete_node_size_decrement():
        test_base = _DoublyLinkedBase()
        test_element = "A"
        # insert new node manually so test is not dependent
        # on _insert_between() method being correct
        new_node = _Node(test_element, test_base._header, test_base._trailer)
        test_base._header._next = new_node
        test_base._trailer._prev = new_node
        test_base._size += 1
        initial_length = len(test_base)
        test_base._delete_node(new_node)
        # test that size decreased
        new_length = len(test_base)
        assert initial_length == new_length + 1

    @staticmethod
    def test_delete_node_return_Value():
        """
        Test that '_delete_node()' correctly returns element associated
        with deleted node.
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        # insert new node manually so test is not dependent
        # on _insert_between() method being correct
        new_node = _Node(test_element, test_base._header, test_base._trailer)
        test_base._header._next = new_node
        test_base._trailer._prev = new_node
        returned_element = test_base._delete_node(new_node)
        # test return value
        assert returned_element == test_element

    @staticmethod
    def test_delete_node_deprecates_node():
        """
        Test that the '_delete_node()' method correctly deprecates the deleted
        node by setting all its attributes to None, so that the node
        can be garbage collected.
        """
        test_base = _DoublyLinkedBase()
        test_element = "A"
        # insert new node manually so test is not dependent
        # on _insert_between() method being correct
        new_node = _Node(test_element, test_base._header, test_base._trailer)
        test_base._header._next = new_node
        test_base._trailer._prev = new_node
        test_base._delete_node(new_node)
        # test deleted node deprecation
        assert new_node._prev is None
        assert new_node._next is None
        assert new_node._element is None
