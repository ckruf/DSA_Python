"""This file contains solution attempt for exercise 7.2"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None


def concatenate_linked_lists(first_head: Node, second_head: Node) -> Node:
    """
    Concatenate two singly linked lists L and M, given only references to the
    first node of each list, into a single list L' that contains all
    the nodes of L followed by all the nodes of M.
    """
    walk = first_head
    while walk._next is not None:
        walk = walk._next
    walk._next = second_head
    return first_head
