"""This file contains tests for exercise 7.4"""
import ch07.my_practice_implementations.singly_linked_list as sl
import ch07.my_practice_implementations.doubly_linked_list as dl
from ch07.my_practice_implementations.positional_list import PositionalList
from ch07.exercises.swap_nodes_4 import (
    swap_nodes_singly_linked,
    swap_nodes_doubly_linked
)

class TestSwapNodesSinglyLinked:
    """
    Tests for 'swap_nodes_singly_linked()' function.
    """

    @staticmethod
    def test_middle_nodes():
        """
        Test the case where:
        - neither node is at the beginning or end of the list
        - nodes are not neighbors
        """
        test_list = sl.LinkedList()
        elems = ["A", "B", "X", "C", "Y", "D"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")
        
        X_node = test_list.get_node_at_index(x_original_position)
        assert isinstance(X_node, sl.Node)
        assert X_node._element == "X"

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        swapped_elems = ["A", "B", "Y", "C", "X", "D"]
        assert swapped_elems == [e for e in test_list]

    @staticmethod
    def test_first_node():
        """
        Test case where:
        - one node is at beginning of the list
        - other node is neither beginning nor end
        - nodes are not neighbors

        Checks (among other) whether ._head gets updated correctly
        """
        test_list = sl.LinkedList()
        elems = ["X", "A", "B", "C", "Y", "D"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")
        
        X_node = test_list.get_node_at_index(x_original_position)
        assert isinstance(X_node, sl.Node)
        assert X_node._element == "X"

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        assert test_list._head == X_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        assert test_list._head == Y_node

        swapped_elems = ["Y", "A", "B", "C", "X", "D"]
        assert swapped_elems == [e for e in test_list]


    @staticmethod
    def test_last_node():
        """
        Test case where
        - one node is at end of the list
        - other node is neither beginning nor end
        - nodes are not neighbors

        Checks (among other) whether ._tail gets updated correctly
        """
        test_list = sl.LinkedList()
        elems = ["A", "B", "X", "C", "D", "Y"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")
        
        X_node = test_list.get_node_at_index(x_original_position)
        assert isinstance(X_node, sl.Node)
        assert X_node._element == "X"

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        assert test_list._tail == Y_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        assert test_list._tail == X_node

        swapped_elems = ["A", "B", "Y", "C", "D", "X"]
        assert swapped_elems == [e for e in test_list]

    @staticmethod
    def test_first_last_node():
        """
        Test case where:
        - one node is at beginning of the list
        - other nodes is at end of the list
        - nodes are not neighbors

        Checks (among other) whether ._head and ._tail get updated correctly
        """
        test_list = sl.LinkedList()
        elems = ["X", "A", "B", "C", "D", "Y"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")
        
        X_node = test_list.get_node_at_index(x_original_position)
        assert isinstance(X_node, sl.Node)
        assert X_node._element == "X"

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        assert test_list._head == X_node
        assert test_list._tail == Y_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        assert test_list._head == Y_node
        assert test_list._tail == X_node

        swapped_elems = elems = ["Y", "A", "B", "C", "D", "X"]
        assert swapped_elems == [e for e in test_list]
        

    @staticmethod
    def test_neighboring_nodes_middle():
        """
        Test case where:
        - nodes are neighboring 
        - neither node is beginning of list or end of list
        """
        test_list = sl.LinkedList()
        elems = ["A", "B", "X", "Y", "C", "D"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")
        
        X_node = test_list.get_node_at_index(x_original_position)
        assert isinstance(X_node, sl.Node)
        assert X_node._element == "X"

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        swapped_elems = ["A", "B", "Y", "X", "C", "D"]
        assert swapped_elems == [e for e in test_list]


    @staticmethod
    def test_neighboring_nodes_beginning():
        """
        Test case where:
        - nodes are neighboring
        - nodes are at start of the list

        Checks (among other) whether ._head gets updated correctly
        """
        test_list = sl.LinkedList()
        elems = ["X", "Y", "A", "B", "C", "D"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")
        
        X_node = test_list.get_node_at_index(x_original_position)
        assert isinstance(X_node, sl.Node)
        assert X_node._element == "X"

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        assert test_list._head == X_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        assert test_list._head == Y_node

        swapped_elems = ["Y", "X",  "A", "B", "C", "D"]
        assert swapped_elems == [e for e in test_list]


    @staticmethod
    def test_neighboring_nodes_end():
        """
        Test case where:
        - nodes are neighboring
        - nodes are at end of list

        Checks (among other) whether ._tail gets updated correctly
        """
        test_list = sl.LinkedList()
        elems = ["A", "B", "C", "D", "X", "Y"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")
        
        X_node = test_list.get_node_at_index(x_original_position)
        assert isinstance(X_node, sl.Node)
        assert X_node._element == "X"

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        assert test_list._tail == Y_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        assert test_list._tail == X_node

        swapped_elems = ["A", "B", "C", "D", "Y", "X"]
        assert swapped_elems == [e for e in test_list]


    @staticmethod
    def test_neighboring_nodes_beginning_and_end():
        """
        Test case where:
        - nodes are neighboring
        - nodes are both at beginning and end of list (ie they are 
        the only two elements in the list)

        Checks (among other) whether ._head and ._tail get updated correctly
        """
        test_list = sl.LinkedList()
        elems = ["X", "Y"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")
        
        X_node = test_list.get_node_at_index(x_original_position)
        assert isinstance(X_node, sl.Node)
        assert X_node._element == "X"

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        swapped_elems = ["Y", "X"]
        assert swapped_elems == [e for e in test_list]



class TestSwapNodesDoublyLinked:
    """
    Tests for function to swap nodes in a doubly linked list.
    """

    @staticmethod
    def test_middle_nodes():
        """
        Test the case where:
        - neither node is at the beginning or end of the list
        - nodes are not neighbors
        """

    @staticmethod
    def test_first_node():
        """
        Test case where:
        - one node is at beginning of the list
        - other node is neither beginning nor end
        - nodes are not neighbors
        """

    @staticmethod
    def test_last_node():
        """
        Test case where
        - one node is at end of the list
        - other node is neither beginning nor end
        - nodes are not neighbors
        """

    @staticmethod
    def test_first_last_node():
        """
        Test case where:
        - one node is at beginning of the list
        - other nodes is at end of the list
        - nodes are not neighbors
        """

    @staticmethod
    def test_neighboring_nodes_middle():
        """
        Test case where:
        - nodes are neighboring 
        - neither node is beginning of list or end of list
        """

    @staticmethod
    def test_neighboring_nodes_beginning():
        """
        Test case where:
        - nodes are neighboring
        - nodes are at start of the list
        """

    @staticmethod
    def test_neighboring_nodes_end():
        """
        Test case where:
        - nodes are neighboring
        - nodes are at end of list
        """

    @staticmethod
    def test_neighboring_nodes_beginning_and_end():
        """
        Test case where:
        - nodes are neighboring
        - nodes are both at beginning and end of list (ie they are 
        the only two elements in the list)

        Checks (among other) whether ._head and ._tail get updated correctly
        """