import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

"""
Our implementation of separate chaining in ChainHashMap conserves
memory by representing empty buckets in the table as None, rather than
as empty instances of a secondary structure. Because many of these buckets will hold a single item, a better optimization is to have those slots of
the table directly reference the Item instance, and to reserve use of secondary containers for buckets that have two or more items. Modify our
implementation to provide this additional optimization.
"""


from typing import Any, Hashable, Union
from ch10.my_practice_implementations.unsorted_table_map import UnsortedTableMap
from ch10.my_practice_implementations.hash_map_base import HashMapBase


class ChainHashMap(HashMapBase):
    _table: list[Union[None, HashMapBase.Item, UnsortedTableMap]]

    def _bucket_getitem(self, j: int, k: Hashable) -> Any:
        slot = self._table[j]
        if slot is None:
            raise KeyError()
        elif isinstance(slot, self.Item):
            if slot._key == k:
                return slot._value
            else:
                # key hashed to same value as existing key, but it's a different key
                raise KeyError()
        else:
            assert isinstance(slot, UnsortedTableMap)
            return slot[k]

    def _bucket_setitem(self, j: int, k: Hashable, v: Any) -> None:
        slot = self._table[j]
        if slot is None:
            self._table[j] = UnsortedTableMap()
        elif isinstance(slot, self.Item):
            if slot._key == k:
                slot._value = v
                return
            else:
                self._table[j] = UnsortedTableMap()
                self._table[j][slot._key] = slot._value
        self._table[j][k] = v

    def _bucket_delitem(self, j: int, k: Hashable) -> None:
        if self._table[j] is None:
            raise KeyError()
        elif isinstance(self._table[j], self.Item):
            if self._table[j]._key == k:
                self._table[j] = None
                return
            else:
                raise KeyError()
        else:
            del self._table[j][k]

    def __iter__(self):
        for i in range(len(self._table)):
            if self._table[i] is not None:
                if isinstance(self._table[i], self.Item):
                    yield self._table[i]._key
                elif isinstance(self._table[i], UnsortedTableMap):
                    for key in self._table[i]:
                        yield key
        