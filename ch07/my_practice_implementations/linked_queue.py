from __future__ import annotations
from typing import Optional, Any


class _Node:
    __slots__ = "_element", "_next"
    _element: Any
    _next: Optional[_Node]

    def __init__(self, element: Any, next: Optional[_Node]):
        self._element = element
        self._next = next


class LinkedQueue:
    _size: int
    _head: Optional[_Node]
    _tail: Optional[_Node]

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def enqueue(self, element: Any) -> None:
        new_end = _Node(element, None)
        if self._size == 0:
            self._head = new_end
        else:
            self._tail._next = new_end
        self._tail = new_end
        self._size += 1

    def dequeue(self) -> Any:
        if self._size == 0:
            raise ValueError("The queue is empty")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        # IMPORTANT SPECIAL CASE!!!!!
        if self._size == 0:
            self._tail = None
        return element

    def front(self) -> Any:
        if self._size == 0:
            raise ValueError("The queue is empty")
        return self._head._element

    def __len__(self) -> Any:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0
