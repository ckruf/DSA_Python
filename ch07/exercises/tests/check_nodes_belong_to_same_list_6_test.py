"""This file contains tests for exercise 7.6"""
import itertools
from ch07.exercises.check_nodes_belong_to_same_list_6 import check_if_nodes_belong_to_same_list
from ch07.my_practice_implementations.circular_list import (
    CircularList,
    Node
)


def test_belong_to_same_list():
    test_list = CircularList()
    test_list.insert_last("A")
    test_list.insert_last("B")
    B_node = test_list._tail
    assert isinstance(B_node, Node)
    assert B_node._element == "B"
    A_node = B_node._next
    assert isinstance(A_node, Node)
    assert A_node._element == "A"

    nodes = [A_node, B_node]
    for node_1, node_2 in itertools.combinations(nodes, 2):
        assert check_if_nodes_belong_to_same_list(node_1, node_2) is True

    test_list.insert_last("C")
    C_node = test_list._tail
    assert isinstance(C_node, Node)
    assert C_node._element == "C"
    nodes.append(C_node)
    for node_1, node_2 in itertools.combinations(nodes, 2):
        assert check_if_nodes_belong_to_same_list(node_1, node_2) is True

    test_list.insert_last("D")
    D_node = test_list._tail
    assert isinstance(D_node, Node)
    assert D_node._element == "D"
    nodes.append(D_node)

    nodes = [A_node, B_node, C_node, D_node]
    for node_1, node_2 in itertools.combinations(nodes, 2):
        assert check_if_nodes_belong_to_same_list(node_1, node_2) is True


def test_dont_belong_to_same_list():
    test_list = CircularList()
    test_list.insert_last("A")
    A_node = test_list._tail
    assert isinstance(A_node, Node)
    assert A_node._element == "A"
    random_node = Node("whatever")
    assert check_if_nodes_belong_to_same_list(A_node, random_node) is False
    test_list.insert_last("B")
    assert check_if_nodes_belong_to_same_list(A_node, random_node) is False
    test_list.insert_last("C")
    assert check_if_nodes_belong_to_same_list(A_node, random_node) is False