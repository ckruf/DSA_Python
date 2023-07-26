"""This file contains solution attempt for exercise 7.24"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None

class LinkedStack:
    """
    Give a complete implementation of the stack ADT using a singly linked
    list that includes a header sentinel
    """
    _header: Node
    _size: int

    def __init__(self):
        self._header = Node(None)
        self._size = 0

    def push(self, e: Any) -> None:
        new_top = Node(e, self._header._next)
        self._header._next = new_top
        self._size += 1

    def pop(self) -> Any:
        if self._size == 0:
            raise Exception("The stack is empty")
        top = self._header._next
        new_top = top._next
        top._next = None
        self._header._next = new_top
        self._size -= 1
        return top._element

    def top(self) -> Any:
        if self._size == 0:
            raise Exception("The stack is empty")
        return self._header._next._element

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size


    