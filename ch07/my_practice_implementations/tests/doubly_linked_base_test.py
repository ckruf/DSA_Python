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
        test_base._insert_between(test_element, test_base._header, test_base._trailer)
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


class TestReverseIterative:
    """
    Tests for the 'reverse_iterative()' method of the DoublyLinkedBase class.
    Done for exercise 7.33
    """

    @staticmethod
    def test_reverse_iterative_non_empty():
        test_base = _DoublyLinkedBase()
        A_node = test_base._insert_between("A", test_base._header, test_base._trailer)
        B_node = test_base._insert_between("B", A_node, test_base._trailer)
        C_node = test_base._insert_between("C", B_node, test_base._trailer)
        original_header = test_base._header
        original_trailer = test_base._trailer

        # make assertions about list before reversing
        assert isinstance(original_header, _Node)
        assert original_header._prev is None
        assert original_header._next == A_node

        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        assert A_node._prev == original_header
        assert A_node._next == B_node

        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        assert B_node._prev == A_node
        assert B_node._next == C_node

        assert isinstance(C_node, _Node)
        assert C_node._element == "C"
        assert C_node._prev == B_node
        assert C_node._next == original_trailer

        assert isinstance(original_trailer, _Node)
        assert original_trailer._prev == C_node
        assert original_trailer._next is None

        test_base.reverse_iterative()

        assert test_base._header == original_trailer
        assert test_base._header._next == C_node
        assert test_base._header._prev is None

        assert C_node._next == B_node
        assert C_node._prev == test_base._header

        assert B_node._next == A_node
        assert B_node._prev == C_node

        assert A_node._next == test_base._trailer
        assert A_node._prev == B_node

        assert test_base._trailer == original_header
        assert test_base._trailer._next is None
        assert test_base._trailer._prev == A_node

    @staticmethod
    def test_reverse_iterative_empty():
        test_base = _DoublyLinkedBase()
        original_header = test_base._header
        original_trailer = test_base._trailer

        assert test_base._header._prev is None
        assert test_base._header._next == test_base._trailer

        assert test_base._trailer._prev == test_base._header
        assert test_base._trailer._next is None

        test_base.reverse_iterative()

        assert test_base._header == original_trailer
        assert test_base._header._next == test_base._trailer
        assert test_base._header._prev is None

        assert test_base._trailer == original_header
        assert test_base._trailer._prev == test_base._header
        assert test_base._trailer._next is None


class TestReverseRecursive:
    """
    Tests for the 'reverse_recursive()' method of the DoublyLinkedBase class.
    Done for exercise 7.33
    """

    @staticmethod
    def test_reverse_recursive_non_empty():
        test_base = _DoublyLinkedBase()
        A_node = test_base._insert_between("A", test_base._header, test_base._trailer)
        B_node = test_base._insert_between("B", A_node, test_base._trailer)
        C_node = test_base._insert_between("C", B_node, test_base._trailer)
        original_header = test_base._header
        original_trailer = test_base._trailer

        # make assertions about list before reversing
        assert isinstance(original_header, _Node)
        assert original_header._prev is None
        assert original_header._next == A_node

        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        assert A_node._prev == original_header
        assert A_node._next == B_node

        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        assert B_node._prev == A_node
        assert B_node._next == C_node

        assert isinstance(C_node, _Node)
        assert C_node._element == "C"
        assert C_node._prev == B_node
        assert C_node._next == original_trailer

        assert isinstance(original_trailer, _Node)
        assert original_trailer._prev == C_node
        assert original_trailer._next is None

        test_base.reverse_recursive()

        assert test_base._header == original_trailer
        assert test_base._header._next == C_node
        assert test_base._header._prev is None

        assert C_node._next == B_node
        assert C_node._prev == test_base._header

        assert B_node._next == A_node
        assert B_node._prev == C_node

        assert A_node._next == test_base._trailer
        assert A_node._prev == B_node

        assert test_base._trailer == original_header
        assert test_base._trailer._next is None
        assert test_base._trailer._prev == A_node

    @staticmethod
    def test_reverse_recursive_empty():
        test_base = _DoublyLinkedBase()
        original_header = test_base._header
        original_trailer = test_base._trailer

        assert test_base._header._prev is None
        assert test_base._header._next == test_base._trailer

        assert test_base._trailer._prev == test_base._header
        assert test_base._trailer._next is None

        test_base.reverse_recursive()

        assert test_base._header == original_trailer
        assert test_base._header._next == test_base._trailer
        assert test_base._header._prev is None

        assert test_base._trailer == original_header
        assert test_base._trailer._prev == test_base._header
        assert test_base._trailer._next is None
