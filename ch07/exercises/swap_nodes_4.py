"""This file contains solution attempt for exercise 7.4"""
from typing import Optional
import ch07.my_practice_implementations.singly_linked_list as sl
import ch07.my_practice_implementations.doubly_linked_list as dl


def swap_nodes_singly_linked(
        linked_list: sl.LinkedList,
        x_node: sl.Node,
        y_node: sl.Node
) -> None:
    """
    Describe in detail how to swap two nodes x and y (not just their contents)
    in a singly linked list L given references only to x and y.
    """
    preceding_x: Optional[sl.Node] = None
    preceding_y: Optional[sl.Node] = None

    walk = linked_list._head
    while walk is not None:
        if walk._next == x_node:
            preceding_x = walk
        elif walk._next == y_node:
            preceding_y = walk
        walk = walk._next
    after_x = x_node._next
    after_y = y_node._next

    # check for None in case x is first node
    if preceding_x is not None:
        preceding_x._next = y_node
    y_node._next = after_x

    if preceding_y is not None:
        preceding_y._next = x_node
    x_node._next = after_y


def swap_nodes_doubly_linked(
        x_node: dl._Node,
        y_node: dl._Node
) -> None:
    preceding_x = x_node._prev
    after_x = x_node._next

    preceding_y = y_node._prev
    after_y = y_node._next

    if preceding_x is not None:
        preceding_x._next = y_node
    if after_x is not None:
        after_x._prev = y_node
    y_node._next = after_x
    y_node._prev = preceding_x

    if preceding_y is not None:
        preceding_y._next = x_node
    if after_y is not None:
        after_y._prev = x_node
    x_node._next = after_y
    x_node._prev = preceding_y