from __future__ import annotations
from typing import Any, Optional


class _Node:
  __slots__ = "_next", "_element"
  _next: Optional[_Node]
  _element: Any

  def __init__(self, element: Any, next: Optional[_Node]):
    self._element = element
    self._next = next


class CircularQueue:
  _tail: Optional[_Node]
  _size: int

  def __init__(self):
    self._tail = None
    self._size = 0

  def enqueue(self, element: Any) -> None:
    new_tail = _Node(element, None)
    if self._size == 0:
      new_tail._next = new_tail
    else:
      new_tail._next = self._tail._next
      self._tail._next = new_tail
    self._size += 1
    self._tail = new_tail

  def dequeue(self) -> Any:
    if self._size == 0:
      raise ValueError("Queue is empty")
    element = self._tail._next._element
    if self._size == 1:
      self._tail = None
    else:
      self._tail._next = self._tail._next._next
    self._size -= 1
    return element

  def rotate(self) -> None:
    if self._size == 0:
      raise ValueError("Queue is empty")
    self._tail = self._tail._next

  def first(self) -> Any:
    if self._size == 0:
      raise ValueError("Queue is empty")
    return self._tail._next._element

  def __len__(self) -> int:
    return self._size

  def is_empty(self) -> bool:
    return self._size == 0
