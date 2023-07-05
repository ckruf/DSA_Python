"""This file contains solution attempt for exercise 7.1"""
from typing import Optional
from ch07.my_practice_implementations import singly_linked_list


def find_penultimate_node(
    linked_list: singly_linked_list.LinkedList
) ->  Optional[singly_linked_list.Node]:
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