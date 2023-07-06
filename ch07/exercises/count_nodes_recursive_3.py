"""This file contains solution attempt for exercise 7.3"""
from typing import Optional
from ch07.my_practice_implementations.singly_linked_list import (
    LinkedList,
    Node
)


def count_nodes(L: LinkedList) -> int:
    """
    Describe a recursive algorithm that counts the number of nodes 
    in a singly linked list.
    """
    def _traverse_and_count(node: Optional[Node], count: int = 0) -> int:
        if node is None:
            return count
        else:
            return _traverse_and_count(node._next, count + 1)
    return _traverse_and_count(L._head)