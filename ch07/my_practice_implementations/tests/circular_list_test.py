import pytest
from ch07.my_practice_implementations.circular_list import (
    CircularList,
    Node
)


class TestInsertFirst:
    """
    Tests for the 'insert_first()' method of the CircularList class.
    """

    @staticmethod
    def test_insert_into_empty_list():
        test_list = CircularList()
        
        assert len(test_list) == 0
        assert test_list._tail is None

        test_list.insert_first("A")
        assert len(test_list) == 1
        A_node = test_list._tail
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert test_list._tail._next == A_node

    @staticmethod
    def test_insert_into_single_element_list():
        test_list = CircularList()
        B_node = Node("B")
        B_node._next = B_node
        test_list._tail = B_node
        test_list._size = 1

        test_list.insert_first("A")

        A_node = test_list._tail._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node
        assert test_list._tail == B_node
        assert len(test_list) == 2

    @staticmethod
    def test_insert_into_multi_element_list():
        test_list = CircularList()
        C_node = Node("C")
        B_node = Node("B")
        C_node._next = B_node
        B_node._next = C_node
        test_list._tail = C_node
        test_list._size = 2

        test_list.insert_first("A")
        A_node = C_node._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node
        assert test_list._tail == C_node
        assert len(test_list) == 3


class TestInsertLast:
    """
    Tests for the 'insert_last()' method of the CircularList class.
    """

    @staticmethod
    def test_insert_into_empty_list():
        test_list = CircularList()
        
        assert len(test_list) == 0
        assert test_list._tail is None

        test_list.insert_last("A")

        A_node = test_list._tail
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == A_node
        assert len(test_list) == 1

    @staticmethod
    def test_insert_into_single_element_list():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._size = 1
        test_list._tail = A_node

        test_list.insert_last("B")
        B_node = test_list._tail
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert B_node._next == A_node
        assert len(test_list) == 2

    @staticmethod
    def test_insert_into_multi_element_list():
        test_list = CircularList()
        A_node = Node("A")
        B_node = Node("B")

        B_node._next = A_node
        A_node._next = B_node
        test_list._tail = B_node
        test_list._size = 2

        test_list.insert_last("C")
        C_node = test_list._tail
        assert isinstance(C_node, Node)
        assert C_node._element == "C"
        assert C_node._next == A_node
        assert B_node._next == C_node
        assert len(test_list) == 3


class TestInsertAfter:
    """
    Tests for the 'insert_after()' method of the CircularList class.
    """

    @staticmethod
    def test_insert_after_only_node():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._tail = A_node
        test_list._size = 1
        
        test_list.insert_after(A_node, "B")

        B_node = test_list._tail._next
        assert isinstance(B_node, Node)
        assert B_node._element == "B"
        assert A_node._next == B_node
        assert B_node._next == A_node
        assert len(test_list) == 2 

    @staticmethod
    def test_insert_after_mulitple_nodes():
        test_list = CircularList()
        B_node = Node("B")
        C_node = Node("C")
        B_node._next = C_node
        C_node._next = B_node
        test_list._size = 2
        test_list._tail = C_node

        test_list.insert_after(C_node, "A")

        A_node = test_list._tail._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"
        assert A_node._next == B_node
        assert C_node._next == A_node
        assert len(test_list) == 3

    @staticmethod
    def test_insert_after_nonexistent():
        """
        Test that the 'insert_after()' method raises an Exception when
        given a node which does not belong to the list.
        """
        test_list = CircularList()
        A_node = Node("A")
        B_node = Node("B")
        C_node = Node("C")
        C_node._next = A_node
        A_node._next = B_node
        B_node._next = C_node
        test_list._tail = C_node
        test_list._size = 3
        
        D_node = Node("D")

        with pytest.raises(ValueError):
            test_list.insert_after(D_node, "E")



class TestDeleleteFirst:
    """
    Tests for the 'delete_first()' method of the CircularList class.
    """

    @staticmethod
    def test_delete_first_empty():
        """
        Test that an exception is raised when 'delete_first()' is called 
        on an empty list.
        """
        test_list = CircularList()
        with pytest.raises(Exception):
            test_list.delete_first()

    @staticmethod
    def test_delete_first_single_element():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._tail = A_node
        test_list._size = 1

        element = test_list.delete_first()
        assert element == "A"
        assert len(test_list) == 0
        assert test_list._tail is None
        assert A_node._next is None

    @staticmethod
    def test_delete_first_mulitple_elements():
        test_list = CircularList()
        for e in "A", "B", "C":
            test_list.insert_last(e)
        # get all nodes first
        C_node = test_list._tail
        assert isinstance(C_node, Node)
        assert C_node._element == "C"

        A_node = C_node._next
        assert isinstance(A_node, Node)
        assert A_node._element == "A"

        B_node = A_node._next 
        assert isinstance(B_node, Node)
        assert B_node._element == "B"

        assert len(test_list) == 3

        result = test_list.delete_first()
        assert result == "A"

        assert test_list._tail == C_node
        assert C_node._next == B_node
        assert B_node._next == C_node
        assert len(test_list) == 2
        assert A_node._next is None


class TestDeleteLast:
    """
    Tests for the 'delete_last()' method of the CircularList class.
    """

    @staticmethod
    def test_delete_last_empty():
        """
        Test that an exception is raised when'delete_last()' is called
        on an empty list.
        """
        test_list = CircularList()
        with pytest.raises(Exception):
            test_list.delete_last()

    @staticmethod
    def test_delete_last_single_element():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._tail = A_node
        test_list._size = 1

        element = test_list.delete_last()
        assert element == "A"
        assert len(test_list) == 0
        assert test_list._tail is None
        assert A_node._next is None

    @staticmethod
    def test_delete_last_mulitple_elements():
        test_list = CircularList()
        
        A_node = Node("A")
        B_node = Node("B")
        C_node = Node("C")
        C_node._next = A_node
        A_node._next = B_node
        B_node._next = C_node
        test_list._tail = C_node
        test_list._size = 3

        element = test_list.delete_last()
        assert element == "C"
        assert test_list._tail == B_node
        assert B_node._next == A_node
        assert C_node._next is None
        assert A_node._next == B_node
        assert len(test_list) == 2


class TestDeleteNode:
    """
    Tests for the 'delete_node()' method of the CircularList class.
    """

    @staticmethod
    def test_delete_node_empty():
        test_list = CircularList()
        with pytest.raises(Exception):
            test_list.delete_node(Node("A"))

    @staticmethod
    def test_delete_node_single_element():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._size = 1
        test_list._tail = A_node
        
        test_list.delete_node(A_node)
        assert test_list._tail is None
        assert len(test_list) == 0

    @staticmethod
    def test_delete_node_multiple_elements():
        test_list = CircularList()
        
        A_node = Node("A")
        B_node = Node("B")
        C_node = Node("C")
        C_node._next = A_node
        A_node._next = B_node
        B_node._next = C_node
        test_list._tail = C_node
        test_list._size = 3

        test_list.delete_node(B_node)
        assert test_list._tail == C_node
        assert C_node._next == A_node
        assert A_node._next == C_node
        assert B_node._next is None
        assert len(test_list) == 2

    @staticmethod
    def test_delete_tail_node_mulitple_elements():
        test_list = CircularList()
        
        A_node = Node("A")
        B_node = Node("B")
        C_node = Node("C")
        C_node._next = A_node
        A_node._next = B_node
        B_node._next = C_node
        test_list._tail = C_node
        test_list._size = 3

        test_list.delete_node(C_node)

        assert test_list._tail == B_node
        assert B_node._next == A_node
        assert A_node._next == B_node
        assert C_node._next is None
        assert len(test_list) == 2

        
    @staticmethod
    def test_delete_non_existent_node():
        test_list = CircularList()
        A_node = Node("A")
        B_node = Node("B")
        C_node = Node("C")
        C_node._next = A_node
        A_node._next = B_node
        B_node._next = C_node
        test_list._tail = C_node
        test_list._size = 3
        
        D_node = Node("D")

        with pytest.raises(ValueError):
            test_list.delete_node(D_node)


class TestFind:
    """
    Tests for the 'find()' method of the CircularList class.
    """

    @staticmethod
    def test_find_in_empty_list():
        test_list = CircularList()
        result = test_list.find("A")
        assert result is None

    @staticmethod
    def test_find_in_single_element_list():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._size = 1
        test_list._tail = A_node

        result = test_list.find("A")
        assert result == A_node

    @staticmethod
    def test_find_nonexistent_in_single_element_list():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._size = 1
        test_list._tail = A_node

        result = test_list.find("B")
        assert result is None

    @staticmethod
    def test_find_in_multi_element_list():
        test_list = CircularList()
        A_node = Node("A")
        B_node = Node("B")
        A_node._next = B_node
        B_node._next = A_node
        test_list._tail = A_node
        test_list._size = 2

        result = test_list.find("A")
        assert result == A_node
        result = test_list.find("B")
        assert result == B_node

        test_list.insert_last("C")
        C_node = test_list._tail
        assert isinstance(C_node, Node)
        assert C_node._element == "C"
        result = test_list.find("C")
        assert result == C_node

        result = test_list.find("D")
        assert result is None


class TestNodeBelongsToList:

    @staticmethod
    def test_node_belongs_to_empty_list():
        test_list = CircularList()
        A_node = Node("A")
        assert test_list._node_belongs_to_list(A_node) is False

    @staticmethod
    def test_node_belongs_to_list_single_element():
        test_list = CircularList()
        A_node = Node("A")
        A_node._next = A_node
        test_list._size = 1 
        test_list._tail = A_node
        assert test_list._node_belongs_to_list(A_node) is True
        B_node = Node("B")
        assert test_list._node_belongs_to_list(B_node) is False

    @staticmethod
    def test_node_belongs_list_two_elements():
        test_list = CircularList()
        A_node = Node("A")
        B_node = Node("B")
        A_node._next = B_node
        B_node._next = A_node
        test_list._tail = B_node
        test_list._size = 2

        assert test_list._node_belongs_to_list(A_node) is True
        assert test_list._node_belongs_to_list(B_node) is True
        assert test_list._node_belongs_to_list(Node("C")) is False


class TestIter:
    """
    Tests for the __iter__() method of the CircularList class.
    """

    @staticmethod
    def test_iter_empty():
        test_list = CircularList()
        for e in test_list:
            assert False
    
    @staticmethod
    def test_iter_single_element():
        test_list = CircularList()
        test_list.insert_last("A")
        assert [e for e in test_list] == ["A", ]

    @staticmethod
    def test_iter_multiple_elements():
        test_list = CircularList()
        elems = ["A", "B", "C"]
        for e in elems:
            test_list.insert_last(e)
        
