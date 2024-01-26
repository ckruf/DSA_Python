import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from typing import Any, Hashable
from .hash_map_base import HashMapBase
from .unsorted_table_map import UnsortedTableMap


class ChainHashMap(HashMapBase):
    _table: list[UnsortedTableMap]

    def _bucket_getitem(self, j: int, k: Hashable) -> Any:
        if self._table[j] is None:
            raise KeyError("Key Error: " + repr(k))
        linear_map = self._table[j]
        return linear_map[k]  # may raise KeyError

    def _bucket_setitem(self, j: int, k: Hashable, v: Any) -> None:
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        linear_map = self._table[j]
        original_size = len(linear_map)
        linear_map[k] = v
        # insertion of new key
        if len(linear_map) > original_size:
            self._n += 1

    def _bucket_delitem(self, j: int, k: Hashable) -> None:
        if self._table[j] is None:
            raise KeyError("Key Error: " + repr(k))
        linear_map = self._table[j]
        # may raise KeyError
        del linear_map[k]

    def __iter__(self):
        for i in range(len(self._table)):
            if self._table[i] is None:
                continue
            for key in self._table[i]:
                yield key