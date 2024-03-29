from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class _Node:
    _element: Any
    _next: Optional[_Node] = None


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

    def rotate(self) -> None:
        """
        Dequeue the first element of the queue and then enqueue it
        at the back of the queue.
        """
        if self._size == 0:
            raise ValueError("The queue is empty")
        elif self._size == 1:
            return
        else:
            first_node = self._head
            self._head = self._head._next
            first_node._next = None
            self._tail._next = first_node
            self._tail = first_node

    def front(self) -> Any:
        if self._size == 0:
            raise ValueError("The queue is empty")
        return self._head._element

    def __len__(self) -> Any:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def concatenate(self, Q2: LinkedQueue) -> None:
        """
        Exercise 7.26

        Implement a method, concatenate(Q2) for the LinkedQueue class that
        takes all elements of LinkedQueue Q2 and appends them to the end of the
        original queue. The operation should run in O(1) time and should result
        in Q2 being an empty queue.
        """
        if Q2 is self:
            raise Exception("Cannot concatenate queue to itself")

        if self._size == 0:
            self._head = Q2._head
        else:
            self._tail._next = Q2._head
        if Q2._size != 0:
            self._tail = Q2._tail
        self._size += Q2._size
        # empty out Q2
        Q2._head = None
        Q2._tail = None
        Q2._size = 0
