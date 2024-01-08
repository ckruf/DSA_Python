import sys
import os
from pathlib import Path
from typing import Any

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from .priority_queue_base import PriorityQueueBase, Item
from ch07.my_practice_implementations.positional_list import PositionalList, Position


class Empty(Exception):
    pass


class HeapPriorityQueue(PriorityQueueBase):
    _data: list[Item]

    def __init__(self):
        self._data = []

    # private helper methods

    def _left(self, parent_index: int) -> int:
        """
        Given the index of the parent node, return the index of the left
        child node.
        """
        return (2 * parent_index) + 1

    def _right(self, parent_index: int) -> int:
        """
        Given the index of the parent node, return the index of the right
        child node.
        """
        return (2 * parent_index) + 2

    def _has_left(self, parent_index: int) -> bool:
        return self._left(parent_index) < len(self._data)

    def _has_right(self, parent_index: int) -> bool:
        return self._right(parent_index) < len(self._data)

    def _parent(self, child_index: int) -> int:
        """
        Given the index of a child node, return the index of the parent
        node.
        """
        return (child_index - 1) // 2

    def __len__(self) -> int:
        return len(self._data)

    def _swap(self, index_1: int, index_2: int) -> None:
        self._data[index_1], self._data[index_2] = self._data[index_2], self._data[index_1]

    def _upheap(self, index: int) -> None:
        parent_index = self._parent(index)
        if index > 0 and self._data[index] < self._data[parent_index]:
            self._swap(index, parent_index)
            self._upheap(parent_index)

    def _downheap(self, index: int) -> None:
        if self._has_left(index):
            left_child_index = self._left(index)
            child_index = left_child_index
            if self._has_right:
                right_child_index = self._right(index)
                if self._data[right_child_index] < self._data[left_child_index]:
                    child_index = right_child_index
            if self._data[index] > self._data[child_index]:
                self._swap(index, child_index)
                self._downheap(child_index)

    # public methods

    def min(self) -> tuple[int, Any]:
        if self.is_empty():
            raise Empty()
        return self._data[0].to_tuple()

    def remove_min(self) -> tuple[int, Any]:
        if self.is_empty():
            raise Empty()
        result = self._data[0].to_tuple()
        self._swap(0, len(self._data) - 1)
        self._data.pop()
        self._downheap(0)
        return result

    def add(self, key: int, value: Any) -> None:
        new_item = Item(key, value)
        self._data.append(new_item)
        self._upheap(len(self._data) - 1)