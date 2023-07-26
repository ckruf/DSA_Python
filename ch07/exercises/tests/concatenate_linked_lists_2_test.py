"""This file contains tests for exercise 7.2"""
from ch07.exercises.concatenate_linked_lists_2 import concatenate_linked_lists, Node


def test_concatenate_linked_lists():
    """
    Test the 'concatenate_linked_lists()' function.
    """
    # create first list
    A_node = Node("A")
    B_node = Node("B")
    C_node = Node("C")
    A_node._next = B_node
    B_node._next = C_node

    # create second list
    D_node = Node("D")
    E_node = Node("E")
    F_node = Node("F")
    D_node._next = E_node
    E_node._next = F_node

    concatenated = concatenate_linked_lists(A_node, D_node)
    elements = []
    walk = concatenated
    while walk is not None:
        elements.append(walk)
        walk = walk._next
    assert elements == [A_node, B_node, C_node, D_node, E_node, F_node]


def test_concatenate_single_element_lists():
    """
    Test the 'concatenate' function with lists containing a single element.
    """
    A_node = Node("A")
    B_node = Node("B")

    concatenated = concatenate_linked_lists(A_node, B_node)
    elements = []
    walk = concatenated
    while walk is not None:
        elements.append(walk)
        walk = walk._next
    assert elements == [A_node, B_node]
