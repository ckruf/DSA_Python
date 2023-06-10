from __future__ import annotations
from typing import Any, Optional

from .doubly_linked_list import _DoublyLinkedBase, _Node


class Position:
  _container: PositionalList
  _node: _Node

  def __init__(self, container, node):
    self._container = container
    self._node = node

  def element(self) -> Any:
    return self._node._element
  
  def __eq__(self, other) -> bool:
    """Return True if position we are given represents the same location"""
    return type(other) is type(self) and other._node is self._node



class PositionalList(_DoublyLinkedBase):

  def _validate(self, p) -> _Node:
    """Validate and return the node associated with a position"""
    if not isinstance(p, Position):
      raise TypeError("p must be of type Position")
    if p._container is not self:
      raise ValueError("p does not belong to this container")
    if p._node._next is None:
      raise ValueError("p is no longer valid")
    return p._node
  
  def _make_position(self, node: _Node) -> Optional[Position]:
    """Return Position instance for given node (or None if sentinel)"""
    if node is self._header or node is self._trailer:
      return None
    return Position(self, node)

  def first(self) -> Position:
    if self.is_empty():
      raise ValueError("The list is empty")
    return self._make_position(self._header._next)

  def last(self) -> Position:
    if self.is_empty():
      raise ValueError("The list is empty")
    return self._make_position(self._trailer._prev)

  def before(self, p: Position) -> Optional[Position]:
    node = self._validate(p)
    return self._make_position(node._prev)

  def after(self, p: Position) -> Position:
    node = self._validate(p)
    return self._make_position(node._next)

  def __iter__(self):
    cursor = self.first()
    while cursor is not None:
      yield cursor.element()
      cursor = self.after(cursor)

  def _insert_between(self, element: Any, predecessor: _Node, successor: _Node) -> Position:
    new_node = super()._insert_between(element, predecessor, successor)
    return self._make_position(new_node)
  
  def add_first(self, element: Any) -> Position:
    return self._insert_between(element, self._header, self._header._next)

  def add_last(self, element: Any) -> Position:
    return self._insert_between(element, self._trailer._prev, self._trailer)

  def add_before(self, p: Position, element: Any) -> Position:
    node = self._validate(p)
    return self._insert_between(element, node._prev, node)

  def add_after(self, p: Position, element: Any) -> Position:
    node = self._validate(p)
    return self._insert_between(element, node, node._next)

  def delete(self, p: Position) -> Any:
    node = self._validate(p)
    return self._delete_node(node)
  
  def replace(self, p: Position, element: Any) -> Any:
    node = self._validate(p)
    original_element = node._element
    node._element = element
    return original_element
  
