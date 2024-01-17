import sys
import os
from pathlib import Path
from typing import Any, Optional

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from ch09.my_practice_implementations.heap import HeapPriorityQueue


class NonRecursiveHeapPQ(HeapPriorityQueue):



    def _lesser_child(self, index: int) -> Optional[int]:
        """
        Given the index of a position, return the index of the lesser child,
        or None if there is no child that's less than the given parent.
        """
        if self._has_left(index):
            left_child_index = self._left(index)
            lesser_child_index = left_child_index
            if self._has_right(index):
                right_child_index = self._right(index)
                if self._data[right_child_index] < self._data[left_child_index]:
                    lesser_child_index = right_child_index
            if self._data[lesser_child_index] < self._data[index]:
                return lesser_child_index

        return None

    def _downheap(self, index: int) -> None:
        lesser_child_index = self._lesser_child(index)
        while lesser_child_index is not None:
            self._swap(index, lesser_child_index)
            index = lesser_child_index
            lesser_child_index = self._lesser_child(index)

    def _upheap(self, index: int) -> None:
        parent_index = self._parent(index)
        while index > 0 and self._data[parent_index] > self._data[index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._parent(index)