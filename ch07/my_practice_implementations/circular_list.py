from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node]


class CircularList:
    _size: int
    _tail: Optional[Node]


    def __init__(self):
        self._size = 0
        self._tail = None

    def is_empty(self) -> bool:
        return self._size == 0
    
    def __len__(self) -> int:
        return self._size
    
    def get_first(self) -> Any:
        pass

    def get_last(self) -> Any:
        pass
    
    def insert_first(self, element: Any) -> None:
        new_head = Node(element, None)
        if self._size == 0:
            self._tail = new_head
            new_head._next = new_head
        else:
            old_head = self._tail._next
            new_head._next = old_head
            self._tail._next = new_head
        self._size += 1

    def insert_last(self, element: Any) -> None:
        new_tail = Node(element, None)

    def insert_after(self, node: Node, element: Any) -> None:
        pass

    def delete_first(self) -> Any:
        pass

    def delete_last(self) -> Any:
        pass

    def delete_node(self, node: Node) -> Any:
        pass

    def find(self, target: Any) -> Optional[Node]:
        pass

    def __str__(self) -> str:
        pass

    def __iter__(self):
        pass