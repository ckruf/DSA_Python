from __future__ import annotations
from typing import Any, Optional, TypeVar, Generic
from dataclasses import dataclass

from .doubly_linked_list import _DoublyLinkedBase, _Node, T


V = TypeVar("V")


@dataclass(eq=False)
class Position(Generic[V]):
    _container: PositionalList[V]
    _node: _Node[V]

    def element(self) -> V:
        return self._node._element

    def __eq__(self, other) -> bool:
        """
        Return True if position we are given represents the same location
        """
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other) -> bool:
        return not (self == other)


class PositionalList(_DoublyLinkedBase[T]):
    def _validate(self, p) -> _Node[T]:
        """Validate and return the node associated with a position"""
        if not isinstance(p, Position):
            raise TypeError("p must be of type Position")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node: _Node) -> Optional[Position[T]]:
        """Return Position instance for given node (or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        return Position(self, node)

    def first(self) -> Position[T]:
        if self.is_empty():
            raise ValueError("The list is empty")
        return self._make_position(self._header._next)

    def last(self) -> Position[T]:
        if self.is_empty():
            raise ValueError("The list is empty")
        return self._make_position(self._trailer._prev)

    def before(self, p: Position[T]) -> Optional[Position[T]]:
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p: Position[T]) -> Position[T]:
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        if self.is_empty():
            return
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(
        self, element: T, predecessor: _Node[T], successor: _Node[T]
    ) -> Position[T]:
        new_node = super()._insert_between(element, predecessor, successor)
        return self._make_position(new_node)

    def add_first(self, element: T) -> Position[T]:
        return self._insert_between(element, self._header, self._header._next)

    def add_last(self, element: T) -> Position[T]:
        return self._insert_between(element, self._trailer._prev, self._trailer)

    def add_before(self, p: Position[T], element: T) -> Position[T]:
        node = self._validate(p)
        return self._insert_between(element, node._prev, node)

    def add_after(self, p: Position[T], element: T) -> Position[T]:
        node = self._validate(p)
        return self._insert_between(element, node, node._next)

    def delete(self, p: Position[T]) -> T:
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p: Position[T], element: T) -> T:
        node = self._validate(p)
        original_element = node._element
        node._element = element
        return original_element
