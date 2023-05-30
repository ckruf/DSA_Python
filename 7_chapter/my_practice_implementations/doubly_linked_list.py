from __future__ import annotations
from typing import Any, Optional


class _Node:
  _next: Optional[_Node]
  _prev: Optional[_Node]
  _element: Any

  def __init__(self, element: Any, prev: Optional[_Node] = None, next: Optional[_Node] = None):
    self._element = element
    self._prev = prev
    self._next = next

  
class _DoublyLinkedBase:
  _header: Optional[_Node]
  _trailer: Optional[_Node]
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

  def _insert_between(self, element: Any, predecessor: _Node, successor: _Node) -> _Node:
    new_node = _Node(element, predecessor, successor)
    predecessor._next = new_node
    successor._prev = new_node
    self._size += 1
    return new_node

  def _delete_node(self, node: _Node) -> Any:
    predecessor = node._prev
    successor = node._next
    element = node._element

    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    node._prev = node._next = node._element = None

    return element
