import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))


from typing import Any, Hashable
from ch10.my_practice_implementations.hash_map_base import HashMapBase



class QuadraticProbeHashMap(HashMapBase):
    """
    Hashmap implementation which uses quadratic probing for collision 
    resolution, and keeps load factor below 0.5
    """
    _AVAIL = object()  # marker placed after deleting item
    _table: list[HashMapBase.Item]

    def _is_available(self, index: int) -> bool:
        return self._table[index] is None or self._table[index] == self._AVAIL
    
    def _find_slot(self, key: Hashable, index: int) -> tuple[bool, int]:
        """
        Start searching for key at given index. Return whether key is found,
        and the first available index at which we could place key-value pair.
        """
        first_available = None
        probes = 0
        while True:
            if self._is_available(index):
                if first_available is None:
                    first_available = index
                if self._table[j] is None:
                    return False, first_available
            elif self._table[index]._key == key:
                return True, index
            probes += 1
            index = (index + (probes ** 2)) % len(self._table) 
            
    def _bucket_getitem(self, j: int, k: Hashable) -> Any:
        success, index = self._find_slot(k, j)
        if success:
            return self._table[index]._value
        raise KeyError("Key Error: " + repr(k))

    def _bucket_setitem(self, j: int, k: Hashable, v: Any) -> None:
        found, index = self._find_slot(k, j)
        # overwriting existing key-value
        if found:
            self._table[j]._value = v
        else:
            self._table[index] = self.Item(k, v)
            self._n += 1

    def _bucket_delitem(self, j: int, k: Hashable) -> None:
        found, index = self._find_slot(k, j)
        if found:
            self._table[index] = self._AVAIL
            self._n -= 1
        else:
            raise KeyError("Key Error: " + repr(k))

    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key