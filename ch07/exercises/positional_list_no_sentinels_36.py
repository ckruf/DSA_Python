"""File containing solution attempt for exercise 7.36"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class Node:
    _element: Any
    _prev: Optional[Node] = None
    _next: Optional[Node] = None


@dataclass(slots=True)
class Position:
    _node: Node
    _container: PositionalList

    def element(self) -> Any:
        return self._node._element
    
    def __eq__(self, other) -> bool:
        return type(other) is type(self) and other._node is self._node
    
    def __ne__(self, other) -> bool:
        return not (self == other)
    


@dataclass(slots=True)
class PositionalList:
    _size: int = 0
    _first: Optional [Node] = None
    _last: Optional[Node] = None

    # private utilities
    def _make_position(self, node: Optional[Node]) -> Optional[Position]:
        if node is None:
            return None
        return Position(node, self)

    def _validate(self, p: Position) -> Node:
        if not isinstance(p, Position):
            raise TypeError("p must be a Position instance")
        if p._container is not self:
            raise ValueError("p must belong to this list")
        return p._node
    
    def _insert_into_empty_list(self, e: Any) -> Position:
        new_node = Node(e)
        self._first = new_node
        self._last = new_node
        self._size += 1
        return self._make_position(new_node)
    
    def _insert_between_nodes(
        self,
        preceding: Node,
        following: Node,
        e: Any
    ) -> Position:
        new_node = Node(e, preceding, following)
        preceding._next = new_node
        following._prev = new_node
        self._size += 1
        return self._make_position(new_node)
    
    def _delete_last_remaining_node(self) -> Any:
        assert self._size == 1
        assert self._first == self._last
        last_node = self._first
        element = last_node._element
        # garbage collect
        last_node._element = None
        self._first = self._last = None
        self._size = 0
        return element

    # public utilities

    def is_empty(self) -> bool:
        return self._size == 0
    
    def __len__(self) -> int:
        return self._size 
    
    def __iter__(self):
        if self._size == 0:
            return
        walk = self._first
        while walk is not None:
            yield walk._element
            walk = walk._next

    # accessors

    def first(self) -> Optional[Position]:
        return self._make_position(self._first)

    def last(self) -> Optional[Position]:
        return self._make_position(self._last)

    def before(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._next)

    # modifiers

    def add_first(self, e: Any) -> Position:
        if self._size == 0:
            return self._insert_into_empty_list(e)
        current_first = self._first
        new_first = Node(e, None, current_first)
        current_first._prev = new_first
        self._first = new_first
        self._size += 1
        return self._make_position(new_first)

    def add_last(self, e: Any) -> Position:
        if self._size == 0:
            return self._insert_into_empty_list(e)
        current_last = self._last
        new_last = Node(e, current_last, None)
        current_last._next = new_last
        self._last = new_last
        self._size += 1
        return self._make_position(new_last)

    def add_before(self, p: Position, e: Any) -> Position:
        following_node = self._validate(p)
        if following_node == self._first:
            return self.add_first(e)
        preceding_node = following_node._prev
        return self._insert_between_nodes(preceding_node, following_node, e)


    def add_after(self, p: Position, e: Any) -> Position:
        preceding_node = self._validate(p)
        if preceding_node == self._last:
            return self.add_last(e)
        following_node = preceding_node._next
        return self._insert_between_nodes(preceding_node, following_node, e)
    
    def delete_first(self) -> Any:
        if self._size == 0:
            raise Exception("Cannot delete from empty list")
        if self._size == 1:
            return self._delete_last_remaining_node()
        following_node = self._first._next
        element = self._first._element
        # garbage collect
        self._first._next = self._first._element = None
        following_node._prev = None
        self._size -= 1
        self._first = following_node
        if self._size == 1:
            self._last = following_node
        return element
    
    def delete_last(self) -> Any:
        if self._size == 0:
            raise Exception("Cannot delete from empty list")
        if self._size == 1:
            return self._delete_last_remaining_node()
        previous_node = self._last._prev
        element = self._last._element
        # garbage collect
        self._last._prev = self._last._next = self._last._element = None
        previous_node._next = None
        self._size -= 1
        self._last = previous_node
        if self._size == 1:
            self._first = previous_node
        return element

    def delete(self, p: Position) -> Any:
        node = self._validate(p)
        if node == self._first:
            return self.delete_first()
        if node == self._last:
            return self.delete_last()
        preceding_node = node._prev
        following_node = node._next
        element = node._element
        # garbage collect
        node._next = node._prev = node._element = None
        preceding_node._next = following_node
        following_node._prev = preceding_node
        self._size -= 1
        return element

    def replace(self, p: Position, e: Any) -> Any:
        node = self._validate(p)
        element = node._element
        node._element = e
        return element

