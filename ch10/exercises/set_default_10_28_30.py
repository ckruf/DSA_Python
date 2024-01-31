"""
On page 406 of Section 10.1.3, we give an implementation of the method
setdefault as it might appear in the MutableMapping abstract base class.
While that method accomplishes the goal in a general fashion, its efficiency is less than ideal. In particular, when the key is new, there will be
a failed search due to the initial use of getitem , and then a subsequent insertion via setitem . For a concrete implementation, such as
the UnsortedTableMap, this is twice the work because a complete scan
of the table will take place during the failed getitem , and then another complete scan of the table takes place due to the implementation of
setitem . A better solution is for the UnsortedTableMap class to override setdefault to provide a direct solution that performs a single search.
Give such an implementation of UnsortedTableMap.setdefault.
C-10.29 Repeat Exercise C-10.28 for the ProbeHashMap class.
C-10.30 Repeat Exercise C-10.28 for the ChainHashMap class.
"""

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
from ch10.my_practice_implementations.unsorted_table_map import UnsortedTableMap
from ch10.my_practice_implementations.linear_probe_hash_map import LinearProbeHashMap
from ch10.my_practice_implementations.chain_hash_map import ChainHashMap


class SetDefaultUnsortedTableMap(UnsortedTableMap):

    def setdefault(self, k, v) -> Any:
        """
        If key is already in table, return corresponding value. 
        Otherwise, create new key-value pair, and return the newly added value
        """
        for item in self._table:
            if item._key == k:
                return item._value
        self._table.append(self.Item(k, v))
        return v


class SetDefaultProbeHashMap(LinearProbeHashMap):

    def setdefault(self, k, v) -> Any:
        j = self._hash_function(k)
        found, index = self._find_slot(j, k)
        if found:
            return self._table[index]._value
        else:
            self._table[index] = self.Item(k, v)
            self._n += 1
            return v


class SetDefaultChainHashMap(ChainHashMap):

    def setdefault(self, k, v) -> Any:
        j = self._hash_function(k)
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        for item in self._table[j]._table:
            if item._key == k:
                return item._value
        self._table[j]._table.append(self.Item(k, v))
        self._n += 1
        return v
            