from __future__ import annotations
from typing import Any, Optional, Generic, TypeVar
from dataclasses import dataclass


X = TypeVar("X")
T = TypeVar("T")


@dataclass(slots=True, repr=False)
class _Node(Generic[X]):
    _element: Optional[X]
    _prev: Optional[_Node[X]] = None
    _next: Optional[_Node[X]] = None

    def __str__(self) -> str:
        first_part= f"_Node(_element={self._element}, "
        if self._prev is None:
            second_part = "_prev=None, "
        else:
            second_part = f"_prev=_Node(_element={self._prev._element}), "
        if self._next is None:
            third_part = "_next=None)"
        else:
            third_part=f"_next=_Node(_element={self._next._element}))"
        return first_part + second_part + third_part
    
    def __repr__(self) -> str:
        return str(self)


class _DoublyLinkedBase(Generic[T]):
    _header: Optional[_Node[T]]
    _trailer: Optional[_Node[T]]
    _size: int

    def __init__(self):
        self._header = _Node(None)
        self._trailer = _Node(None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def _insert_between(
        self, element: Any, predecessor: _Node[T], successor: _Node[T]
    ) -> _Node[T]:
        new_node = _Node(element, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node: _Node) -> T:
        predecessor = node._prev
        successor = node._next
        element = node._element

        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        node._prev = node._next = node._element = None

        return element
