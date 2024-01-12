import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from typing import Any
from ch09.my_practice_implementations.heap import HeapPriorityQueue


class PQQueue:
    _data: HeapPriorityQueue
    _count: int

    def __init__(self):
        self._data = HeapPriorityQueue()
        self._count = 0

    def enqueue(self, e: Any) -> None:
        self._data.add(self._count, e)
        self._count += 1

    def dequeue(self) -> Any:
        _, value = self._data.remove_min()
        return value

    def front(self) -> Any:
        _, value = self._data.min()
        return value

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return self._data.is_empty()
