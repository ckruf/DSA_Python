"""This file contains solution attempt for exercise 7.1"""
from typing import Optional
from ch07.my_practice_implementations.singly_linked_list import (
    LinkedList,
    Node
    )


def find_penultimate_node(linked_list: LinkedList) ->  Optional[Node]:
    """
    Exercise 7.1
    Find the second-to-last node in a singly linked list in which the last
    node is indicated by a next reference of None.
    """
    if len(linked_list) < 2:
        return None
    walk = linked_list._head
    while walk._next._next is not None:
        walk = walk._next
    return walk


def find_penultimate_node_recursive(linked_list: LinkedList) -> Optional[Node]:
    def _recursive_traversal(current_node: Node) -> Optional[Node]:
        # empty or single element list
        if current_node is None or current_node._next is None:
            return None
        elif current_node._next._next is None:
            return current_node
        else:
            return _recursive_traversal(current_node._next)
    return _recursive_traversal(linked_list._head)