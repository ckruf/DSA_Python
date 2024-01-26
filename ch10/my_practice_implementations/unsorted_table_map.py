import sys
import os
from pathlib import Path
from typing import Any

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from ch10.my_practice_implementations.map_base import MapBase


class UnsortedTableMap(MapBase):
    """
    Map implementation using Python list, with O(n) complexity for all operations.
    """
    _table: list[MapBase.Item]

    def __init__(self):
        self._table = []

    def __getitem__(self, k) -> Any:
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError("Key Error: " + repr(k))
    
    def __setitem__(self, k, v) -> None:
        for item in self._table:
            if item._key == k:
                item._value = v
                return
        self._table.append(self.Item(k, v))

    def __delitem__(self, k) -> None:
        for i in range(self._table):
            if self._table[i]._key == k:
                self._table.pop(i)
                return
        raise KeyError("Key Error: " + repr(k))
    
    def __len__(self) -> int:
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield item._key



    
