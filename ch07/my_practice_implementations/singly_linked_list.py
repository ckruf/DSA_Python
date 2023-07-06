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
        if index == 0:
            self.add_first(element)
            return
        if index == self._size:
            self.add_last(element)
            return
        if not 0 < index < self._size:
            raise ValueError(
                f"index must be between 0 and {self._size} (inclusive)"
            )
        # get to node at index - 1
        count = 0
        walk = self._head
        while count < index - 1:
            walk = walk._next
            count += 1
        # insert after node at index - 1
        newly_inserted = Node(element, walk._next)
        walk._next = newly_inserted
        self._size += 1
        
    def delete_first(self) -> Any:
        """Delete the first node of the list"""
        if self._size == 0:
            raise ValueError("Cannot remove first, list is empty")
        current_head = self._head
        self._head = self._head._next
        element = current_head.element()
        current_head._element = current_head._next = None
        self._size -= 1
        if self._size == 0:
            self._head = None
            self._tail = None
        return element
    
    def delete_last(self) -> Any:
        """Delete the last node of the list"""
        if self._size == 0:
            raise ValueError("Cannot remove last, list is empty")
        if self._size == 1:
            element = self._head.element()
            self._head = None
            self._tail = None
            self._size -= 1
            return element
        walk = self._head
        while walk._next._next is not None:
            walk = walk._next
        element = self._tail.element()
        # deprecate node
        self._tail._element = self._tail._next = None
        self._tail = walk
        self._tail._next = None
        self._size -= 1
        return element
        
    def delete_at_index(self, index: int) -> Any:
        """Delete the node at the given index"""
        if index == 0:
            return self.delete_first()
        if index == self._size - 1:
            return self.delete_last()
        if not 0 <= index < self._size:
            raise ValueError(
                f"index must be greater than 0 and less than {self._size}"
            )
        count = 0
        walk = self._head
        while count < index - 1:
            walk = walk._next
            count += 1
        deleted_node = walk._next
        element = deleted_node._element
        walk._next = deleted_node._next
        deleted_node._next = deleted_node._element = None  # garbage collection / node invalidation
        self._size -= 1
        return element
    
    def get_first(self) -> Any:
        """Get first element of linked list"""
        if self._size == 0:
            raise ValueError("Cannot get first, list is empty")
        return self._head.element()
    
    def get_last(self) -> Any:
        """Get the last element of linked list"""
        if self._size == 0:
            raise ValueError("Cannot get last, list is empty")
        return self._tail.element()
    
    def __iter__(self):
        walk = self._head
        while walk is not None:
            yield walk.element()
            walk = walk._next
    
    def __str__(self) -> str:
        return str([i for i in self])
    
    def clear(self) -> None:
        walk = self._head
        while walk is not None:
            next = walk._next
            walk._next = None
            walk._element = None
            walk = next
        self._head = None
        self._tail = None
        self._size = 0
