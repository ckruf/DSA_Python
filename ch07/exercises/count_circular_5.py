"""This file contains solution attempt for exercise 7.5"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any
from ch07.my_practice_implementations.circular_list import CircularList, Node


def count_nodes_circular(test_list: CircularList) -> int:
    """
    Implement a function that counts the number of nodes in a circularly
    linked list.
    """
    if test_list._tail is None:
        return 0
    count = 1
    walk = test_list._tail._next
    while walk != test_list._tail:
        count += 1
        walk = walk._next
    return count
