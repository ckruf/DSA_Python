"""File containing solution attempt for exercise 7.32"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


class Empty(Exception):
    pass


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None
    _prev: Optional[Node] = None

    def __repr__(self):
        prev_ = None
        if self._prev:
            prev_ = self._prev._element
        next_ = None
        if self._next:
            next_ = self._next._element

        return f"Node(element={self._element}, prev={prev_}, next={next_})"

    def __str__(self):
        prev_ = None
        if self._prev:
            prev_ = self._prev._element
        next_ = None
        if self._next:
            next_ = self._next._element

        return f"Node(element={self._element}, prev={prev_}, next={next_})"


@dataclass(slots=True)
class Position:
    _node: Node
    _container: Optional[CircularPositionalList]

    def element(self) -> Any:
        return self._node._element

    def __eq__(self, other) -> bool:
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other) -> bool:
        return not (other == self)


class CircularPositionalList:
    _size: int
    _cursor: Optional[Node]

    def __init__(self):
        self._size = 0
        self._cursor = None

    def _validate(self, p: Position) -> Node:
        if not isinstance(p, Position):
            raise TypeError("p must be a Position instance")
        if p._container is not self:
            raise ValueError("p must belong to this list")
        if p._node._next is None:
            raise ValueError("p is deprecated")
        return p._node

    def _make_position(self, node: Optional[Node]) -> Optional[Position]:
        if node is None:
            return None
        return Position(node, self)

    def current_element(self) -> Optional[Position]:
        return self._make_position(self._cursor)

    def next_element(self, p: Optional[Position] = None) -> Optional[Position]:
        if self._size == 0:
            raise Empty("Can't get element after cursor in empty list")
        if p:
            node = self._validate(p)
        else:
            node = self._cursor
        return self._make_position(node._next)

    def previous_element(self, p: Optional[Position] = None) -> Optional[Position]:
        if self._size == 0:
            raise Empty("Can't get element before cursor in empty list")
        if p:
            node = self._validate(p)
        else:
            node = self._cursor
        return self._make_position(node._prev)

    def move_next(self) -> None:
        if self._size == 0:
            raise Empty("Can't move cursor in empty list")
        self._cursor = self._cursor._next

    def move_previous(self) -> None:
        if self._size == 0:
            raise Empty("Can't move cursor in empty list")
        self._cursor = self._cursor._prev

    def add_after(self, e: Any) -> None:
        new_cursor = Node(e)
        if self._size == 0:
            new_cursor._next = new_cursor
            new_cursor._prev = new_cursor
        else:
            new_cursor._next = self._cursor._next
            new_cursor._prev = self._cursor
            self._cursor._next._prev = new_cursor
            self._cursor._next = new_cursor
        self._cursor = new_cursor
        self._size += 1

    def add_before(self, e: Any) -> None:
        new_cursor = Node(e)
        if self._size == 0:
            new_cursor._next = new_cursor
            new_cursor._prev = new_cursor
        else:
            new_cursor._next = self._cursor
            new_cursor._prev = self._cursor._prev
            self._cursor._prev._next = new_cursor
            self._cursor._prev = new_cursor
        self._cursor = new_cursor
        self._size += 1

    def delete(self) -> Any:
        if self._size == 0:
            raise Empty("Can't delete from empty list")
        elif self._size == 1:
            self._cursor._next = None
            self._cursor._prev = None
            element = self._cursor._element
            self._cursor._element = None
            self._cursor = None
        else:
            preceding_node = self._cursor._prev
            following_node = self._cursor._next
            self._cursor._prev = None
            self._cursor._next = None
            element = self._cursor._element
            self._cursor._element = None
            following_node._prev = preceding_node
            preceding_node._next = following_node
            self._cursor = following_node
        self._size -= 1
        return element

    def replace(self, e: Any) -> Any:
        if self._size == 0:
            raise ValueError("Can't replace cursor element in empty list")
        element = self._cursor._element
        self._cursor._element = e
        return element

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def __iter__(self):
        if self._size == 0:
            return
        else:
            walk = self._cursor
            while True:
                yield walk._element
                if walk._next == self._cursor:
                    break
                walk = walk._next
