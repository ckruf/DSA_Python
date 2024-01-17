from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Item:
    _key: int
    _value: Any

    def __lt__(self, other: Item):
        assert type(other) is type(self)
        return self._key < other._key

    def to_tuple(self) -> tuple[int, Any]:
        return self._key, self._value


class Empty(Exception):
    pass


class SortedPriorityQueue:
    """
    Priority queue implemented using a sorted python list as underlying storage.
    min() and remove_min() are O(1)
    add() is O(n)
    """
    _data: list[Item]

    def __init__(self):
        self._data = []

    def add(self, key: int, value: Any) -> None:
        new_item = Item(key, value)
        n = len(self._data)
        index = 0
        while index < n and self._data[index] > new_item:
            index += 1
        self._data.insert(index, new_item)

    def min(self) -> tuple[int, Any]:
        if self.is_empty():
            raise Empty()
        return self._data[len(self._data)-1].to_tuple()

    def remove_min(self) -> tuple[int, Any]:
        if self.is_empty():
            raise Empty()
        return self._data.pop().to_tuple()

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return len(self._data)


if __name__ == "__main__":
    pq = SortedPriorityQueue()
    pq.add(5, 'A')
    pq.add(3, 'B')
    pq.add(7, 'C')
    assert pq.remove_min() == (3, 'B')
    assert len(pq) == 2
    assert pq.min() == (5, 'A')