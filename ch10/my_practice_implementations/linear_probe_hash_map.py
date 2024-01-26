import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from typing import Any, Hashable, Optional
from .hash_map_base import HashMapBase
from .map_base import MapBase


class LinearProbeHashMap(HashMapBase):
    _table: list[Optional[MapBase.Item]]
    _AVAIL = object()

    def _is_available(self, j: int) -> bool:
        """Is the slot at index j available?"""
        return self._table[j] is None or self._table[j] == self._AVAIL

    def _find_slot(self, j: int, k: Hashable) -> tuple[bool, int]:
        """
        Start searching for key k at index j, and continue probing.
        If key k is found, return True, index of k.
        If key k is not found (we run into None), return False and 
        the first available index at which k can be placed.
        
        Because load factor is kept < 0.5, this loop cannot be infinite.
        """
        while True:
            first_available = None
            if self._is_available(j):
                if first_available is None:
                    first_available = j
                if self._table[j] is None:
                    return False, first_available
            elif self._table[j]._key == k:
                return True, j
            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j: int, k: Hashable) -> Any:
        success, index = self._find_slot(j, k)
        if success:
            return self._table[index]._value
        raise KeyError("Key Error: " + repr(k))

    def _bucket_setitem(self, j: int, k: Hashable, v: Any) -> None:
        success, index = self._find_slot(j, k)
        # key already in table, overwrite
        if success:
            self._table[index]._value = v
        else:
            self._table[index] = self.Item(k, v)
            self._n += 1

    def _bucket_delitem(self, j: int, k: Hashable) -> None:
        success, index = self._find_slot(j, k)
        if not success:
            raise KeyError("Key Error: " + repr(k))
        else:
            self._table[index] = self._AVAIL
            self._n -= 1

    def __iter__(self):
        for i in range(len(self._table)):
            if self._is_available(i):
                continue
            yield self._table[i]._key