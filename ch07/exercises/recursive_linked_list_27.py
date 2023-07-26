from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


class RecursiveLinkedList:
    _element: Any
    _rest: Optional[RecursiveLinkedList]

    def __init__(
        self,
        element: Any = None,
        rest: Optional[RecursiveLinkedList] = None
    ):
        self._element = element
        self._rest = rest

    def is_empty(self) -> bool:
        return self._element is None

    def __len__(self) -> int:
        if self._element is None:
            return 0
        elif self._rest is None:
            return 1
        else:
            return 1 + len(self._rest)

    def add_first(self, element: Any) -> RecursiveLinkedList:
        # inserting into empty list
        if self._element is None:
            self._element = element
        else:
            self._rest = RecursiveLinkedList(self._element, self._rest)
            self._element = element
        return self

    def add_last(self, element: Any) -> RecursiveLinkedList:
        if self._element is None:
            self._element = element
        elif self._rest is None:
            self._rest = RecursiveLinkedList(element)
        else:
            self._rest.add_last(element)
        return self

    def delete_first(self) -> RecursiveLinkedList:
        if self._element is None:
            raise Exception("Cannot delete from empty list")
        elif self._rest is None:
            self._element = None
        else:
            self._element = self._rest._element
            self._rest = self._rest._rest
        return self

    def delete_last(self) -> RecursiveLinkedList:
        if self._element is None:
            raise Exception("Cannot delete from empty list")
        elif self._rest is None:
            self._element = None
        elif self._rest._rest is None:
            self._rest = None
        else:
            self._rest.delete_last()
        return self

    def first(self) -> Any:
        if self._element is None:
            raise Exception("List is empty")
        return self._element

    def last(self) -> Any:
        if self._element is None:
            raise Exception("List is empty")
        if self._rest is None:
            return self._element
        else:
            return self._rest.last()

    def __iter__(self):
        pass

    def __str__(self) -> str:
        pass