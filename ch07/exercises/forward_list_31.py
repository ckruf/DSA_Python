"""File containing solution attempt for exercise 7.31"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None


@dataclass(slots=True)
class Position:
    _container: Optional[ForwardList]
    _node: Node

    def element(self) -> Any:
        return self._node._element

    def __eq__(self, other):
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
        return not (self == other)


class ForwardList:
    """
    Abstraction of a singly linked list.
    """

    _size: int
    _header: Node

    def __init__(self):
        self._size = 0
        self._header = Node(None)

    def _validate(self, p: Position) -> Node:
        if not isinstance(p, Position):
            raise TypeError("p must be a Position instance!")
        if p._container is not self:
            raise ValueError("p must belong to this list")
        return p._node

    def _make_position(self, node: Optional[Node]) -> Optional[Position]:
        if node is None:
            return None
        return Position(self, node)

    def first(self) -> Optional[Position]:
        return self._make_position(self._header._next)

    def after(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._next)

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        walk = self.first()
        while walk is not None:
            yield walk.element()
            walk = self.after(walk)

    def add_first(self, e: Any) -> Position:
        current_first = self._header._next
        new_first = Node(e, current_first)
        self._header._next = new_first
        self._size += 1
        return self._make_position(new_first)

    def add_after(self, p: Position, e: Any) -> Position:
        node = self._validate(p)
        new_following_node = Node(e, node._next)
        node._next = new_following_node
        self._size += 1
        return self._make_position(new_following_node)

    def replace(self, p: Position, e: Any) -> Any:
        node = self._validate(p)
        current_element = node._element
        node._element = e
        return current_element

    def delete(self, p: Position) -> None:
        node_for_deletion = self._validate(p)
        walk = self._header
        while walk is not None and walk._next != node_for_deletion:
            walk = walk._next
        if walk._next != node_for_deletion:
            raise ValueError("Given position is not in the list")
        preceding_node = walk
        preceding_node._next = node_for_deletion._next
        node_for_deletion._next = node_for_deletion._element = None
        self._size -= 1
