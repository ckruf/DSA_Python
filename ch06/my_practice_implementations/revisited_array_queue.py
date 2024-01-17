from typing import Any


class Empty(Exception):
    pass


class ArrayQueue:
    INITIAL_SIZE = 10
    _size: int
    _data: list[Any]
    _front: int

    def __init__(self):
        self._size = 0
        self._data = [None] * self.INITIAL_SIZE
        self._front = 0

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Empty("Cannot dequeue from empty queue")
        front_item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return front_item

    def enqueue(self, e: Any) -> None:
        if self._size == len(self._data):
            self._resize(2 * self._size)
        end = (self._front + self._size) % len(self._data)
        self._data[end] = e
        self._size += 1

    def first(self) -> Any:
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return self._size

    def _resize(self, new_capacity: int) -> None:
        if new_capacity < self._size:
            raise ValueError(f"Cannot resize to {new_capacity}, queue has {self._size} elements")
        old_data = self._data
        self._data = [None] * new_capacity
        for i in range(self._size):
            index = (self._front + i) % len(old_data)
            self._data[i] = old_data[index]
        self._front = 0
