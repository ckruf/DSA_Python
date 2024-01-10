import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from typing import Any, Optional
from ch09.my_practice_implementations.unsorted_priority_queue import (
    UnsortedPriorityQueue,
    Item,
    Empty
)


class QuickMinUnsortedPQ(UnsortedPriorityQueue):
    """
    Priority queue implemented using an unsorted list, modified such that
    `min()` has O(1) complexity.
    """
    _min_item: Optional[Item]

    def __init__(self):
        self._min_item = None
        super().__init__()

    def add(self, key: int, value: Any) -> None:
        new_item = Item(key, value)
        if self._min_item is None or new_item < self._min_item:
            self._min_item = new_item
        self._data.add_last(new_item)

    def min(self) -> tuple[int, Any]:
        if self._min_item is None:
            raise Empty()
        return self._min_item.to_tuple()
    
    def remove_min(self) -> tuple[int, Any]:
        current_min_item = super().remove_min()
        new_min_tem = self._find_min()
        self._min_tem = new_min_tem
        return current_min_item