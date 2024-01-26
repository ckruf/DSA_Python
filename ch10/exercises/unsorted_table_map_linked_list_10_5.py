import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))

from typing import Any
from ch07.my_practice_implementations.positional_list import PositionalList
from ch10.my_practice_implementations.map_base import MapBase


class UnsortedLinkedTableMap(MapBase):
    """
    Map implementation using linked list, with O(n) complexity for all operations
    """

    _table: PositionalList[MapBase.Item]

    def __init__(self):
        self._table = PositionalList()

    def __getitem__(self, k) -> Any:
        if not self._table.is_empty():
            walk = self._table.first()
            while walk is not None:
                item = walk.element()
                if item._key == k:
                    return item._value
                walk = self._table.after(walk)
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v) -> None:
        if not self._table.is_empty():
            walk = self._table.first()
            while walk is not None:
                item = walk.element()
                if item._key == k:
                    item._value = v
                    return
        self._table.add_last(self.Item(k, v))

    def __delitem__(self, k) -> None:
        if not self._table.is_empty():
            walk = self._table.first()
            while walk is not None:
                item = walk.element()
                if item._key == k:
                    self._table.delete(walk)
                    return
        raise KeyError("Key Error: " + repr(k))

    
    def __len__(self) -> int:
        return len(self._table)
    
    def __iter__(self):
        if not self._table.is_empty():
            walk = self._table.first()
            while walk is not None:
                yield walk.element()._key
                walk = self._table.after(walk)
