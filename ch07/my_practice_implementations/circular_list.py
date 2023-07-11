from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass(slots=True)
class Node:
    _element: Any
    _next: Optional[Node] = None


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
        if self._size == 0:
            raise Exception("List is empty")
        return self._tail._next._element

    def get_last(self) -> Any:
        if self._size == 0:
            raise 
        return self._tail._element
    
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
        if self._size == 0:
            new_tail._next = new_tail
        else:
            new_tail._next = self._tail._next
            self._tail._next = new_tail
        self._tail = new_tail
        self._size += 1

    def insert_after(self, node: Node, element: Any) -> None:
        if not self._node_belongs_to_list(node):
            raise ValueError("Given node does not belong to this list")
        new_node = Node(element)
        new_node._next = node._next
        node._next = new_node
        self._size += 1


    def delete_first(self) -> Any:
        if self._size == 0:
            raise Exception("Can't delete from empty list")
        element = self._tail._next._element
        if self._size == 1:
            self._tail._next = self._tail = None
        else:
            first_node = self._tail._next
            self._tail._next = self._tail._next._next
            first_node._next = None
        self._size -= 1
        return element
    
    def delete_last(self) -> Any:
        if self._size == 0:
            raise ValueError("Can't delete from empty list")
        element = self._tail._element
        if self._size == 1:
            self._tail._next = self._tail = None
        else:
            penultimate_node = None
            walk = self._tail
            while walk._next != self._tail:
                walk = walk._next
            penultimate_node = walk
            penultimate_node._next = self._tail._next
            self._tail._next = None  # garbage collect
            self._tail = penultimate_node
        self._size -= 1
        return element

    def delete_node(self, node: Node) -> None:
        if self._size == 0:
            raise ValueError("Can't delete from empty list")
        elif self._size == 1:
            if self._tail != node:
                raise ValueError("Node is not part of list")
            self._tail._next = self._tail = None
        else:
            if node == self._tail:
                return self.delete_last()
            walk = self._tail
            preceding_node = None
            while walk._next != node:
                walk = walk._next
                if walk == self._tail:
                    raise ValueError("Node is not part of list")
            preceding_node = walk
            preceding_node._next = node._next
            node._next = None
        self._size -= 1

    def find(self, target: Any) -> Optional[Node]:
        if self._size == 0:
            return None
        walk = self._tail
        while walk._element != target:
            walk = walk._next
            if walk == self._tail:
                return None
        return walk
    
    def _node_belongs_to_list(self, node: Node) -> bool:
        if self._size == 0:
            return False
        if node == self._tail:
            return True
        walk = self._tail._next
        while walk != self._tail:
            if walk == node:
                return True
            walk =  walk._next
        return False

    def __str__(self) -> str:
        pass

    def __iter__(self):
        if self._size == 0:
            return
        walk = self._tail._next
        while True: 
            yield walk._element
            if walk == self._tail:
                break
            walk = walk._next