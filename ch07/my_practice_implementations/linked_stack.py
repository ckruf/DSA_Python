from __future__ import annotations
from typing import Any, Optional


class _Node:
    __slots__ = "_element", "_next"
    _element: Any
    _next: Optional[_Node]

    def __init__(self, element: Any, next: Optional[_Node]):
        self._element = element
        self._next = next


class LinkedStack:
    _head: Optional[_Node]
    _size: int

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, element: Any) -> None:
        new_top = _Node(element, self._head)
        self._head = new_top
        self._size += 1

    def pop(self) -> Any:
        if self._size == 0:
            raise ValueError("Stack is empty")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element

    def top(self) -> Any:
        if self._size == 0:
            raise ValueError("Stack is empty")
        return self._head._element

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0
