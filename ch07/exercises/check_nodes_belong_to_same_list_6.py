"""This file contains solution attempt for exercise 7.6"""
from ch07.my_practice_implementations.circular_list import Node


def check_if_nodes_belong_to_same_list(
    A_node: Node,
    B_node: Node
) -> bool:
    """
    Check whether two nodes, each of which belongs to a circular list,
    belong to the same (circular) list.
    """
    walk = A_node._next
    while True:
        if walk == B_node:
            return True
        if walk == A_node:
            return False
        walk = walk._next