from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None

    def element(self) -> Any:
        return self._element


class LinkedList:
    _head: Optional[Node]
    _tail: Optional[Node]
    _size: int

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0
    
    def __len__(self) -> int:
        return self._size
    
    def add_first(self, element: Any) -> None:
        """Insert an item at the beginning of the list."""
        new_head = Node(element, self._head)
        self._head = new_head
        if self._size == 0:
            self._tail = new_head
        self._size += 1

    def add_last(self, element: Any) -> None:
        """Insert an item at the end of the list."""
        new_tail = Node(element)
        if self._size == 0:
            self._head = new_tail
        else:
            self._tail._next = new_tail
        self._tail = new_tail
        self._size += 1

    def add_at_index(self, element: Any, index: int) -> None:
        """
        Insert item at a given position. The item will be inserted before
        the item currently at the given index, and so it will become the 
        item at that index after insertion. For example:

        add_at_index(x, 0) will insert the item at the front of the list
        add_(x, len(list)) will insert the item at the end of the list
        """
        if not 0 <= index <= self._size:
            raise ValueError(
                f"index must be between 0 and {self._size} (inclusive)"
            )
        count = 0
        walk = self._head
        while count < index:
            walk = walk._next
        

    

    

