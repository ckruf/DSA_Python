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

        # node originally before x
        before_X = test_list.get_node_at_index(x_original_position - 1)
        assert isinstance(before_X, sl.Node)
        assert before_X._element == elems[x_original_position - 1]
        assert before_X._next == X_node

        # node originally after x
        after_X = test_list.get_node_at_index(x_original_position + 1)
        assert isinstance(after_X, sl.Node)
        assert after_X._element == elems[x_original_position + 1]
        assert X_node._next == after_X

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        # node originally before y
        before_Y = test_list.get_node_at_index(y_original_position - 1)
        assert isinstance(before_Y, sl.Node)
        assert before_Y._element == elems[y_original_position - 1]
        assert before_Y._next == Y_node

        # node originally after y
        after_Y = test_list.get_node_at_index(y_original_position + 1)
        assert isinstance(after_Y, sl.Node)
        assert after_Y._element == elems[y_original_position + 1]
        assert Y_node._next == after_Y

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointers on either side of X after swap
        assert before_Y._next == X_node
        assert X_node_moved._next == after_Y

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointers on either side of Y after swap
        assert before_X._next == Y_node
        assert Y_node_moved._next == after_X

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

        # node originally after x
        after_X = test_list.get_node_at_index(x_original_position + 1)
        assert isinstance(after_X, sl.Node)
        assert after_X._element == elems[x_original_position + 1]
        assert X_node._next == after_X

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        # node originally before y
        before_Y = test_list.get_node_at_index(y_original_position - 1)
        assert isinstance(before_Y, sl.Node)
        assert before_Y._element == elems[y_original_position - 1]
        assert before_Y._next == Y_node

        # node originally after y
        after_Y = test_list.get_node_at_index(y_original_position + 1)
        assert isinstance(after_Y, sl.Node)
        assert after_Y._element == elems[y_original_position + 1]
        assert Y_node._next == after_Y

        assert test_list._head == X_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointers on either side of X after swap
        assert before_Y._next == X_node
        assert X_node_moved._next == after_Y

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointer after Y after swap
        assert Y_node_moved._next == after_X

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

        # node originally before x
        before_X = test_list.get_node_at_index(x_original_position - 1)
        assert isinstance(before_X, sl.Node)
        assert before_X._element == elems[x_original_position - 1]
        assert before_X._next == X_node

        # node originally after x
        after_X = test_list.get_node_at_index(x_original_position + 1)
        assert isinstance(after_X, sl.Node)
        assert after_X._element == elems[x_original_position + 1]
        assert X_node._next == after_X

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        # node originally before y
        before_Y = test_list.get_node_at_index(y_original_position - 1)
        assert isinstance(before_Y, sl.Node)
        assert before_Y._element == elems[y_original_position - 1]
        assert before_Y._next == Y_node

        assert test_list._tail == Y_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointer before X after swap
        assert before_Y._next == X_node

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointers on either side of Y after swap
        assert before_X._next == Y_node
        assert Y_node_moved._next == after_X

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

        # node originally after x
        after_X = test_list.get_node_at_index(x_original_position + 1)
        assert isinstance(after_X, sl.Node)
        assert after_X._element == elems[x_original_position + 1]
        assert X_node._next == after_X

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        # node originally before y
        before_Y = test_list.get_node_at_index(y_original_position - 1)
        assert isinstance(before_Y, sl.Node)
        assert before_Y._element == elems[y_original_position - 1]
        assert before_Y._next == Y_node

        assert test_list._head == X_node
        assert test_list._tail == Y_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        assert before_Y._next == X_node

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        assert Y_node._next == after_X

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

        # node originally before x
        before_X = test_list.get_node_at_index(x_original_position - 1)
        assert isinstance(before_X, sl.Node)
        assert before_X._element == elems[x_original_position - 1]
        assert before_X._next == X_node

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        # node originally after y
        after_Y = test_list.get_node_at_index(y_original_position + 1)
        assert isinstance(after_Y, sl.Node)
        assert after_Y._element == elems[y_original_position + 1]
        assert Y_node._next == after_Y

        # pointer between X and Y before swap
        assert X_node._next == Y_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        assert X_node._next == after_Y

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        assert before_X._next == Y_node

        # pointer between X and Y after swap
        assert Y_node._next == X_node

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

        # node originally after y
        after_Y = test_list.get_node_at_index(y_original_position + 1)
        assert isinstance(after_Y, sl.Node)
        assert after_Y._element == elems[y_original_position + 1]
        assert Y_node._next == after_Y

        # pointer between X and Y before swap
        assert X_node._next == Y_node

        assert test_list._head == X_node

        swap_nodes_singly_linked(test_list, X_node, Y_node)

        X_node_moved = test_list.get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, sl.Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        assert X_node._next == after_Y

        Y_node_moved = test_list.get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, sl.Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        # pointer between X and Y after swap
        assert Y_node._next == X_node

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

        # node originally before x
        before_X = test_list.get_node_at_index(x_original_position - 1)
        assert isinstance(before_X, sl.Node)
        assert before_X._element == elems[x_original_position - 1]
        assert before_X._next == X_node

        Y_node = test_list.get_node_at_index(y_original_position)
        assert isinstance(Y_node, sl.Node)
        assert Y_node._element == "Y"

        # pointer between X and Y before swap
        assert X_node._next == Y_node

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
        assert before_X._next == Y_node

        # pointer between X and Y after swap
        assert Y_node._next == X_node

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

        # pointer between X and Y before swap
        assert X_node._next == Y_node

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

        # pointer between X and Y after swap
        assert Y_node._next == X_node

        assert test_list._head == Y_node
        assert test_list._tail == X_node

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
        test_list = PositionalList()
        elems = ["A", "B", "X", "C", "Y", "D"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")

        X_node = test_list._get_node_at_index(x_original_position)
        assert isinstance(X_node, dl._Node)
        assert X_node._element == "X"

        # node originally before x
        before_X = test_list._get_node_at_index(x_original_position - 1)
        assert isinstance(before_X, dl._Node)
        assert before_X._element == elems[x_original_position - 1]
        assert before_X._next == X_node
        assert X_node._prev == before_X

        # node originally after x
        after_X = test_list._get_node_at_index(x_original_position + 1)
        assert isinstance(after_X, dl._Node)
        assert after_X._element == elems[x_original_position + 1]
        assert X_node._next == after_X
        assert after_X._prev == X_node

        Y_node = test_list._get_node_at_index(y_original_position)
        assert isinstance(Y_node, dl._Node)
        assert Y_node._element == "Y"

        # node originally before y
        before_Y = test_list._get_node_at_index(y_original_position - 1)
        assert isinstance(before_Y, dl._Node)
        assert before_Y._element == elems[y_original_position - 1]
        assert before_Y._next == Y_node
        assert Y_node._prev == before_Y

        # node originally after y
        after_Y = test_list._get_node_at_index(y_original_position + 1)
        assert isinstance(after_Y, dl._Node)
        assert after_Y._element == elems[y_original_position + 1]
        assert Y_node._next == after_Y
        assert after_Y._prev == Y_node

        swap_nodes_doubly_linked(X_node, Y_node)

        X_node_moved = test_list._get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, dl._Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointers on either side of X after swap
        assert before_Y._next == X_node
        assert X_node._prev == before_Y

        assert X_node._next == after_Y
        assert after_Y._prev == X_node

        Y_node_moved = test_list._get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, dl._Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointers on either side of Y after swap
        assert before_X._next == Y_node
        assert Y_node._prev == before_X

        assert Y_node._next == after_X
        assert after_X._prev == Y_node

        swapped_elems = ["A", "B", "Y", "C", "X", "D"]
        assert swapped_elems == [e for e in test_list]


    @staticmethod
    def test_first_node():
        """
        Test case where:
        - one node is at beginning of the list
        - other node is neither beginning nor end
        - nodes are not neighbors
        """
        test_list = PositionalList()
        elems = ["X", "A", "B", "C", "Y", "D"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")

        X_node = test_list._get_node_at_index(x_original_position)
        assert isinstance(X_node, dl._Node)
        assert X_node._element == "X"

        # node originally after x
        after_X = test_list._get_node_at_index(x_original_position + 1)
        assert isinstance(after_X, dl._Node)
        assert after_X._element == elems[x_original_position + 1]
        assert X_node._next == after_X
        assert after_X._prev == X_node

        Y_node = test_list._get_node_at_index(y_original_position)
        assert isinstance(Y_node, dl._Node)
        assert Y_node._element == "Y"

        # node originally before y
        before_Y = test_list._get_node_at_index(y_original_position - 1)
        assert isinstance(before_Y, dl._Node)
        assert before_Y._element == elems[y_original_position - 1]
        assert before_Y._next == Y_node
        assert Y_node._prev == before_Y

        # node originally after y
        after_Y = test_list._get_node_at_index(y_original_position + 1)
        assert isinstance(after_Y, dl._Node)
        assert after_Y._element == elems[y_original_position + 1]
        assert Y_node._next == after_Y
        assert after_Y._prev == Y_node

        assert test_list.first()._node == X_node

        swap_nodes_doubly_linked(X_node, Y_node)

        X_node_moved = test_list._get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, dl._Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointers on either side of X after swap
        assert before_Y._next == X_node
        assert X_node._prev == before_Y

        assert X_node._next == after_Y
        assert after_Y._prev == X_node

        Y_node_moved = test_list._get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, dl._Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointers after Y after swap
        assert Y_node._next == after_X
        assert after_X._prev == Y_node

        assert test_list.first()._node == Y_node

        swapped_elems = ["Y", "A", "B", "C", "X", "D"]
        assert swapped_elems == [e for e in test_list]


    @staticmethod
    def test_last_node():
        """
        Test case where
        - one node is at end of the list
        - other node is neither beginning nor end
        - nodes are not neighbors
        """
        test_list = PositionalList()
        elems = ["A", "B", "X", "C", "D", "Y"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")

        X_node = test_list._get_node_at_index(x_original_position)
        assert isinstance(X_node, dl._Node)
        assert X_node._element == "X"

        # node originally before x
        before_X = test_list._get_node_at_index(x_original_position - 1)
        assert isinstance(before_X, dl._Node)
        assert before_X._element == elems[x_original_position - 1]
        assert before_X._next == X_node
        assert X_node._prev == before_X

        # node originally after x
        after_X = test_list._get_node_at_index(x_original_position + 1)
        assert isinstance(after_X, dl._Node)
        assert after_X._element == elems[x_original_position + 1]
        assert X_node._next == after_X
        assert after_X._prev == X_node

        Y_node = test_list._get_node_at_index(y_original_position)
        assert isinstance(Y_node, dl._Node)
        assert Y_node._element == "Y"

        # node originally before y
        before_Y = test_list._get_node_at_index(y_original_position - 1)
        assert isinstance(before_Y, dl._Node)
        assert before_Y._element == elems[y_original_position - 1]
        assert before_Y._next == Y_node
        assert Y_node._prev == before_Y

        assert test_list.last()._node == Y_node

        swap_nodes_doubly_linked(X_node, Y_node)

        X_node_moved = test_list._get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, dl._Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointers before X after swap
        assert before_Y._next == X_node
        assert X_node._prev == before_Y

        Y_node_moved = test_list._get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, dl._Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointers on either side of Y after swap
        assert before_X._next == Y_node
        assert Y_node._prev == before_X

        assert Y_node._next == after_X
        assert after_X._prev == Y_node

        assert test_list.last()._node == X_node

        swapped_elems = ["A", "B", "Y", "C", "D", "X"]
        assert swapped_elems == [e for e in test_list]

    @staticmethod
    def test_first_last_node():
        """
        Test case where:
        - one node is at beginning of the list
        - other nodes is at end of the list
        - nodes are not neighbors
        """
        test_list = PositionalList()
        elems = ["X", "A", "B", "C", "D", "Y"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")

        X_node = test_list._get_node_at_index(x_original_position)
        assert isinstance(X_node, dl._Node)
        assert X_node._element == "X"

        # node originally after x
        after_X = test_list._get_node_at_index(x_original_position + 1)
        assert isinstance(after_X, dl._Node)
        assert after_X._element == elems[x_original_position + 1]
        assert X_node._next == after_X
        assert after_X._prev == X_node

        Y_node = test_list._get_node_at_index(y_original_position)
        assert isinstance(Y_node, dl._Node)
        assert Y_node._element == "Y"

        # node originally before y
        before_Y = test_list._get_node_at_index(y_original_position - 1)
        assert isinstance(before_Y, dl._Node)
        assert before_Y._element == elems[y_original_position - 1]
        assert before_Y._next == Y_node
        assert Y_node._prev == before_Y

        assert test_list.first()._node == X_node
        assert test_list.last()._node == Y_node

        swap_nodes_doubly_linked(X_node, Y_node)

        X_node_moved = test_list._get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, dl._Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointers before X after swap
        assert before_Y._next == X_node
        assert X_node._prev == before_Y

        Y_node_moved = test_list._get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, dl._Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointers after Y after swap
        assert Y_node._next == after_X
        assert after_X._prev == Y_node

        assert test_list.first()._node == Y_node
        assert test_list.last()._node == X_node

        swapped_elems = ["Y", "A", "B", "C", "D", "X"]
        assert swapped_elems == [e for e in test_list]


    @staticmethod
    def test_neighboring_nodes_middle():
        """
        Test case where:
        - nodes are neighboring 
        - neither node is beginning of list or end of list
        """
        test_list = PositionalList()
        elems = ["A", "B", "X", "Y", "C", "D"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")

        X_node = test_list._get_node_at_index(x_original_position)
        assert isinstance(X_node, dl._Node)
        assert X_node._element == "X"

        # node originally before x
        before_X = test_list._get_node_at_index(x_original_position - 1)
        assert isinstance(before_X, dl._Node)
        assert before_X._element == elems[x_original_position - 1]
        assert before_X._next == X_node
        assert X_node._prev == before_X

        Y_node = test_list._get_node_at_index(y_original_position)
        assert isinstance(Y_node, dl._Node)
        assert Y_node._element == "Y"

        # node originally after y
        after_Y = test_list._get_node_at_index(y_original_position + 1)
        assert isinstance(after_Y, dl._Node)
        assert after_Y._element == elems[y_original_position + 1]
        assert Y_node._next == after_Y
        assert after_Y._prev == Y_node

        # pointers between X and Y before swap
        assert X_node._next == Y_node
        assert Y_node._prev == X_node

        swap_nodes_doubly_linked(X_node, Y_node)

        X_node_moved = test_list._get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, dl._Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointers after X after swap
        assert X_node._next == after_Y
        assert after_Y._prev == X_node

        Y_node_moved = test_list._get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, dl._Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointers before Y after swap
        assert before_X._next == Y_node
        assert Y_node._prev == before_X

        # pointers between X and Y after swap
        assert Y_node._next == X_node
        assert X_node._prev == Y_node

        swapped_elems = ["A", "B", "Y", "X", "C", "D"]
        assert swapped_elems == [e for e in test_list]

    @staticmethod
    def test_neighboring_nodes_beginning():
        """
        Test case where:
        - nodes are neighboring
        - nodes are at start of the list
        """
        test_list = PositionalList()
        elems = ["X", "Y", "A", "B", "C", "D"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")

        X_node = test_list._get_node_at_index(x_original_position)
        assert isinstance(X_node, dl._Node)
        assert X_node._element == "X"

        Y_node = test_list._get_node_at_index(y_original_position)
        assert isinstance(Y_node, dl._Node)
        assert Y_node._element == "Y"

        # node originally after y
        after_Y = test_list._get_node_at_index(y_original_position + 1)
        assert isinstance(after_Y, dl._Node)
        assert after_Y._element == elems[y_original_position + 1]
        assert Y_node._next == after_Y
        assert after_Y._prev == Y_node

        # pointers between X and Y before swap
        assert X_node._next == Y_node
        assert Y_node._prev == X_node
        
        assert test_list.first()._node == X_node

        swap_nodes_doubly_linked(X_node, Y_node)

        X_node_moved = test_list._get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, dl._Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved
        # check pointers after X after swap
        assert X_node._next == after_Y
        assert after_Y._prev == X_node

        Y_node_moved = test_list._get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, dl._Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        # pointers between X and Y after swap
        assert Y_node._next == X_node
        assert X_node._prev == Y_node

        assert test_list.first()._node == Y_node

        swapped_elems = ["Y", "X", "A", "B", "C", "D"]
        assert swapped_elems == [e for e in test_list]

    @staticmethod
    def test_neighboring_nodes_end():
        """
        Test case where:
        - nodes are neighboring
        - nodes are at end of list
        """
        test_list = PositionalList()
        elems = ["A", "B","C", "D", "X", "Y"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")

        X_node = test_list._get_node_at_index(x_original_position)
        assert isinstance(X_node, dl._Node)
        assert X_node._element == "X"

        # node originally before x
        before_X = test_list._get_node_at_index(x_original_position - 1)
        assert isinstance(before_X, dl._Node)
        assert before_X._element == elems[x_original_position - 1]
        assert before_X._next == X_node
        assert X_node._prev == before_X

        Y_node = test_list._get_node_at_index(y_original_position)
        assert isinstance(Y_node, dl._Node)
        assert Y_node._element == "Y"

        # pointers between X and Y before swap
        assert X_node._next == Y_node
        assert Y_node._prev == X_node

        assert test_list.last()._node == Y_node

        swap_nodes_doubly_linked(X_node, Y_node)

        X_node_moved = test_list._get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, dl._Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list._get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, dl._Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved
        # check pointers before Y after swap
        assert before_X._next == Y_node
        assert Y_node._prev == before_X

        # pointers between X and Y after swap
        assert Y_node._next == X_node
        assert X_node._prev == Y_node

        assert test_list.last()._node == X_node

        swapped_elems = ["A", "B","C", "D", "Y", "X"]
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
        test_list = PositionalList()
        elems = ["X", "Y"]
        for e in elems:
            test_list.add_last(e)
        assert elems == [e for e in test_list]

        x_original_position = elems.index("X")
        y_original_position = elems.index("Y")

        X_node = test_list._get_node_at_index(x_original_position)
        assert isinstance(X_node, dl._Node)
        assert X_node._element == "X"

        Y_node = test_list._get_node_at_index(y_original_position)
        assert isinstance(Y_node, dl._Node)
        assert Y_node._element == "Y"

        assert test_list.first()._node == X_node
        assert test_list.last()._node == Y_node

        # nodes between X and Y before swap
        assert X_node._next == Y_node
        assert Y_node._prev == X_node

        swap_nodes_doubly_linked(X_node, Y_node)

        X_node_moved = test_list._get_node_at_index(y_original_position)
        assert isinstance(X_node_moved, dl._Node)
        assert X_node._element == "X"
        assert X_node == X_node_moved

        Y_node_moved = test_list._get_node_at_index(x_original_position)
        assert isinstance(Y_node_moved, dl._Node)
        assert Y_node_moved._element == "Y"
        assert Y_node == Y_node_moved

        # nodes between X and Y after swap
        assert Y_node._next == X_node
        assert X_node._prev == Y_node

        assert test_list.first()._node == Y_node
        assert test_list.last()._node == X_node

        swapped_elems = ["Y", "X"]
        assert swapped_elems == [e for e in test_list]