"""This file contains solution attempt for exercise 7.4"""
from typing import Optional
import ch07.my_practice_implementations.singly_linked_list as sl
import ch07.my_practice_implementations.doubly_linked_list as dl


def swap_nodes_singly_linked(
    linked_list: sl.LinkedList, x_node: sl.Node, y_node: sl.Node
) -> None:
    """
    Describe in detail how to swap two nodes x and y (not just their contents)
    in a singly linked list L given references only to x and y.
    """
    if x_node._next == y_node or y_node._next == x_node:
        return swap_neighboring_nodes_singly_linked(linked_list, x_node, y_node)

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
    if after_x is None:
        linked_list._tail = y_node

    after_y = y_node._next
    if after_y is None:
        linked_list._tail = x_node

    # check for None in case x is first node
    if preceding_x is not None:
        preceding_x._next = y_node
    else:
        linked_list._head = y_node
    y_node._next = after_x

    if preceding_y is not None:
        preceding_y._next = x_node
    else:
        linked_list._head = x_node
    x_node._next = after_y


def swap_neighboring_nodes_singly_linked(
    linked_list: sl.LinkedList, x_node: sl.Node, y_node: sl.Node
) -> None:
    """
    Dedicated helper function for swapping neighboring nodes in a
    singly linked list.
    """
    if x_node._next == y_node:
        first_neighbor = x_node
        second_neighbor = y_node
    elif y_node._next == x_node:
        first_neighbor = y_node
        second_neighbor = x_node
    else:
        raise ValueError("nodes must be neighbors")

    before_neighbors: Optional[sl.Node] = None
    after_neighbors: Optional[sl.Node] = second_neighbor._next

    if first_neighbor != linked_list._head:
        walk = linked_list._head
        while walk._next != first_neighbor:
            walk = walk._next
        before_neighbors = walk

    if before_neighbors is not None:
        before_neighbors._next = second_neighbor
    else:
        linked_list._head = second_neighbor

    if after_neighbors is None:
        linked_list._tail = first_neighbor

    second_neighbor._next = first_neighbor
    first_neighbor._next = after_neighbors


def swap_nodes_doubly_linked(x_node: dl._Node, y_node: dl._Node) -> None:
    """
    Swapping two nodes in a doubly linked list. Note that this function assumes
    a doubly linked list implementation which has header and trailer sentinel
    nodes - it does not work with None on previous/next pointers.
    """
    preceding_x: dl._Node = x_node._prev
    after_x: dl._Node = x_node._next
    # check assumption of sentinel nodes
    assert preceding_x is not None
    assert after_x is not None

    preceding_y: dl._Node = y_node._prev
    after_y: dl._Node = y_node._next
    # check assumption of sentinel nodesS
    assert preceding_y is not None
    assert after_y is not None

    if after_x == y_node or after_y == x_node:
        return swap_neighboring_nodes_doubly_linked(x_node, y_node)

    preceding_x._next = y_node
    after_x._prev = y_node

    y_node._next = after_x
    y_node._prev = preceding_x

    preceding_y._next = x_node
    after_y._prev = x_node

    x_node._next = after_y
    x_node._prev = preceding_y


def swap_neighboring_nodes_doubly_linked(x_node: dl._Node, y_node: dl._Node) -> None:
    """
    Dedicated helper function for swapping neighboring nodes in a doubly
    linked list.
    Note that this function assumes a doubly linked list implementation which
    has header and trailer sentinel nodes - it does not work with None on
    previous/next pointers.
    """
    if x_node._next == y_node:
        first_neighbor = x_node
        second_neighbor = y_node
    elif y_node._next == x_node:
        first_neighbor = y_node
        second_neighbor = x_node
    else:
        raise ValueError("nodes must be neighbors")

    before_neighbors: dl._Node = first_neighbor._prev
    after_neighbors: dl._Node = second_neighbor._next

    # take care of pointer of preceding node
    before_neighbors._next = second_neighbor

    # take care of pointers of first neighbor
    first_neighbor._prev = second_neighbor
    first_neighbor._next = after_neighbors

    # take care of pointers of second neighbor
    second_neighbor._prev = before_neighbors
    second_neighbor._next = first_neighbor

    # take care of pointer of following node
    after_neighbors._prev = first_neighbor
