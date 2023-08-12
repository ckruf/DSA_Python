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
    
    def _get_node_at_index(self, index: int) -> _Node:
        """
        Get node at given index. This method really only serves for making
        testing of 'swap_nodes' method easier. Nodes are abstracted
        away in this implementation, and should not be exposed to the user.
        That's why method is private - only to be used in testing.
        """
        if not 0 <= index < self._size:
            raise ValueError(
                f"index must be 0 or greater and less than {self._size}"
            )
        count = 0
        walk = self._header._next
        while count < index:
            walk = walk._next
            count += 1
        return walk

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
        # necessary because .first() will fail on empty list
        if self.is_empty():
            return
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # class PositionalListIterator:
    #     """
    #     Nested iterator class implemented for exercise 7.35. For this to work,
    #     the __iter__() method below this class (meaning the __iter__() method
    #     belonging to the PositionalList class, not to this class) must be
    #     uncommented.
    #     """
        
    #     def __init__(self, walk: _Node, trailer: _Node):
    #         self.walk = walk
    #         self.trailer = trailer

    #     def __iter__(self):
    #         return self
        
    #     def __next__(self):
    #         if self.walk == self.trailer:
    #             raise StopIteration
    #         else:
    #             element = self.walk._element
    #             self.walk = self.walk._next
    #             return element
            
    # def __iter__(self):
    #     return PositionalList.PositionalListIterator(
    #         self._header._next,
    #         self._trailer
    #     )


    def __reversed__(self):
        if self.is_empty():
            return
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

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
    
    def __str__(self) -> str:
        elements = [i for i in self]
        return str(elements)
    
    def max(self) -> Any:
        maximum = self.first().element()
        for e in self:
            if e > maximum:
                maximum = e
        return maximum

    def find(self, e: Any) -> Optional[Position]:
        walk = self._header._next
        while walk != self._trailer:
            if walk._element == e:
                return self._make_position(walk)
            walk = walk._next
        return None
    
    def find_recursive(self, e: Any) -> Optional[Position]:
        def _find(e: Any, node: _Node) -> _Node:
            if node._element == e or node == self._trailer:
                return node
            else:
                return _find(e, node._next)
        return self._make_position(_find(e, self._header._next))
    
    def add_last_composite(self, element: T) -> Position[T]:
        if self.is_empty():
            return self.add_first(element)
        return self.add_after(self.last(), element)

    def add_before_composite(self, p: Position[T], element: T) -> Position[T]:
        if p == self.first():
            return self.add_first(element)
        else:
            preceding = self.before(p)
            return self.add_after(preceding, element)

    def move_to_front(self, p: Position) -> None:
        """
        Exercise 7.17 - move given node to front by relinking nodes,
        rather than deleting at current position and adding at front.
        """
        if p == self.first():
            return
        
        node = self._validate(p)
        # grab references to all nodes whose pointers need to be relinked
        preceding = node._prev
        following = node._next
        first = self._header._next
        header = self._header
        
        # relink preceding and following node to skip given node now
        preceding._next = following
        following._prev = preceding
        
        # relink given node itself
        node._prev = header
        node._next = first

        # relink header and first node
        header._next = node
        first._prev = node
