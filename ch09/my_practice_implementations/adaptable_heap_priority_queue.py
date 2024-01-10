import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from dataclasses import dataclass
from typing import Any
from ch09.my_practice_implementations.heap import HeapPriorityQueue, Item


@dataclass(slots=True)
class Locator(Item):
    _index: int


class AdapatableHeapPriorityQueue(HeapPriorityQueue):
    _data: list[Locator]

    def _bubble(self, index: int) -> None:
        if index > 0 and self._data[index] < self._data[self._parent(index)]:
            self._upheap(index)
        else:
            self._downheap(index)

    def add(self, key: int, value: Any) -> Locator:
        new_item = Locator(key, value, len(self._data))
        self._data.append(new_item)
        self._upheap(len(self._data)-1)
        return new_item

    def _swap(self, index_1: int, index_2: int) -> None:
        item_1 = self._data[index_1]
        item_2 = self._data[index_2]
        item_1._index = index_2
        item_2._index = index_1
        self._data[index_1], self._data[index_2] = self._data[index_2], self._data[index_1]

    def update(self, loc: Locator, new_key: int, new_value: Any) -> None:
        item = self._data[loc._index]
        item._key = new_key
        item._value = new_value
        self._bubble(loc._index)

    def remove(self, loc: Locator) -> None:
        index = loc._index
        if not (0 <= index < len(self) and self._data[index] is loc):
            raise ValueError(f"Invalid locator {loc}")
        if index == len(self._data) - 1:
            self._data.pop()
        else:
            self._swap(index, len(self._data)-1)
            self._data.pop()
            self._bubble(index)
        return loc.to_tuple()

