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


class PQStack:
    _data: HeapPriorityQueue

    def __init__(self):
        self._data = HeapPriorityQueue()

    def __len__(self) -> int:
        return len(self._data)

    def push(self, e: Any) -> None:
        key = -len(self)
        self._data.add(key, e)

    def pop(self) -> Any:
        _, value = self._data.remove_min()
        return value

    def top(self) -> Any:
        _, value = self._data.min()
        return value
        
    def is_empty(self) -> bool:
        return self.is_empty()

if __name__ == "__main__":
    stack = PQStack()
    letters = ["A", "B", "C", "D", "E"]
    for l in letters:
        stack.push(l)
    for l in reversed(letters):
        assert l == stack.pop()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    assert stack.pop() == "C"
    stack.push("D")
    assert stack.pop() == "D"
    assert stack.pop() == "B"
    assert stack.pop() == "A"