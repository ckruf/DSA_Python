"""This file contains solution attempt for exercise 7.30"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None



class LinkedLeakyStack:
    DEFAULT_SIZE = 5
    """
    Stack with a maximum capacity. When pushing onto a full stack, 'leak'
    the bottom item in the stack. Implemented using singly linked list, per
    exercise requirements. Although this doesn't really make sense because
    pushing onto full stack is O(n).
    """
    _top: Optional[Node]
    _size: int
    _capacity: int

    def __init__(self, capacity: Optional[int] = None):
        if capacity is None:
            capacity = self.DEFAULT_SIZE
        if capacity < 1:
            raise ValueError("Capacity of stack must be at least 1")
        self._top = None
        self._size = 0
        self._capacity = capacity

    def push(self, element: Any) -> None:
        # if at full capacity, 'leak' bottom element
        if self._size == self._capacity:
            if self._capacity == 1:
                self._top = Node(element)
                return
            walk = self._top
            while walk._next._next is not None:
                walk = walk._next
            walk._next = None
            self._size -= 1
        new_top = Node(element)
        new_top._next = self._top
        self._top = new_top
        self._size += 1

    def pop(self) -> Any:
        if self._size == 0:
            raise Exception("Cannot pop from empty stack")
        element = self._top._element
        self._top = self._top._next
        self._size -= 1
        return element

    def top(self) -> Any:
        if self._size == 0:
            raise Exception("Stack is empty")
        return self._top._element

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0
    
    def __iter__(self):
        if self._size == 0:
            return
        walk = self._top
        while walk is not None:
            yield walk._element
            walk = walk._next
    
    def __str__(self) -> str:
        return str([e for e in self])