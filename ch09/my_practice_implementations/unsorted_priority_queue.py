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


class UnsortedPriorityQueue(PriorityQueueBase):
    """
    Priority queue implemented using an unsorted doubly linked list.
    add() is O(1), as we just append to the end.
    min() and remove_min() is O(n) as we need to scan the entire list.
    """
    _data: PositionalList[Item]

    def __init__(self):
        self._data = PositionalList()

    def add(self, key: int, value: Any) -> None:
        item = Item(key, value)
        self._data.add_last(item)

    def _find_min(self) -> Position[Item]:
        if self.is_empty():
            raise Empty()
        walk = self._data.first()
        smallest = walk
        while walk is not None:
            if walk.element() < smallest.element():
                smallest = walk
            walk = self._data.after(walk)
        return smallest

    def min(self) -> tuple[int, Any]:
        smallest = self._find_min()
        return smallest.element().to_tuple()

    def remove_min(self) -> tuple[int, Any]:
        smallest = self._find_min()
        answer = smallest.element().to_tuple()
        self._data.delete(smallest)
        return answer

    def __len__(self) -> int:
        return len(self._data)