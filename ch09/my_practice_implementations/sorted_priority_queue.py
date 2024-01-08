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


class SortedPriorityQueue(PriorityQueueBase):
    _data: PositionalList[Item]

    def __init__(self):
        self._data = PositionalList()

    def add(self, key: int, value: Any) -> None:
        new_item = Item(key, value)
        walk = self._data.last()
        while walk is not None and new_item < walk.element():
            walk = self._data.before(walk)
        if walk is None:  # takes care of empty lists and insertions of new lowest key items
            self._data.add_first(new_item)
        else:
            self._data.add_after(walk, new_item)
        
    def remove_min(self) -> tuple[int, Any]:
        if self.is_empty():
            raise Empty()
        item = self._data.delete(self._data.first())
        return item.to_tuple()

    def min(self) -> tuple[int, Any]:
        if self.is_empty():
            raise Empty()
        first = self._data.first()
        return first.element().to_tuple()

    def __len__(self) -> int:
        return len(self._data)