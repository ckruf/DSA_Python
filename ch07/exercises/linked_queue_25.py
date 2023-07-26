"""This file contains solution attempt for exercise 7.25"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None


class LinkedQueue:
    _header: Node
    _tail: Node
    _size: int

    def __init__(self):
        self._header = Node(None)
        self._tail = self._header
        self._size = 0

    def enqueue(self, e: Any) -> None:
        new_tail = Node(e)
        self._tail._next = new_tail
        self._tail = new_tail
        self._size += 1

    def dequeue(self) -> Any:
        if self._size == 0:
            raise Exception("Queue is empty")
        elif self._size == 1:
            self._tail = self._header
        first_node = self._header._next
        self._header._next = first_node._next
        first_node._next = None  # garbage collect
        self._size -= 1
        return first_node._element

    def first(self) -> Any:
        if self._size == 0:
            raise Exception("Queue is empty")
        return self._header._next._element

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size
