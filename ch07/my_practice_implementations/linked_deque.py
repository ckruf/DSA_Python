from typing import Optional, Any
from .doubly_linked_list import _Node, _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
    def first(self) -> _Node:
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._header._next

    def last(self) -> _Node:
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._trailer._prev

    def insert_first(self, element: Any) -> None:
        self._insert_between(element, self._header, self._header._next)

    def insert_last(self, element) -> None:
        self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_first(self) -> Any:
        if self.is_empty():
            raise ValueError("Deque is empty")
        self._delete_node(self._header._next)

    def delete_last(self) -> Any:
        if self.is_empty():
            raise ValueError("Deque is empty")
        self._delete_node(self._trailer._prev)
