"""This file contains solution attempt for exercise 7.5"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None


def count_nodes_circular(node: Node) -> int:
    """
    Implement a function that counts the number of nodes in a circularly
    linked list.
    """
    count = 1
    walk = node._next
    while walk != node:
        count += 1
        walk = walk._next
    return count