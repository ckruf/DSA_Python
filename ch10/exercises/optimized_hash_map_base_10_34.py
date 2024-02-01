from __future__ import annotations
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, Hashable, Optional
from ch10.my_practice_implementations.hash_map_base import HashMapBase


"""
Computing a hash code can be expensive, especially for lengthy keys. In
our hash table implementations, we compute the hash code when first inserting an item, and recompute each items hash code each time we resize
our table. Pythons dict class makes an interesting trade-off. The hash
code is computed once, when an item is inserted, and the hash code is
stored as an extra field of the item composite, so that it need not be recomputed. Reimplement our HashTableBase class to use such an approach.
"""


class OptimizedHashMapBase(HashMapBase):
    """
    Base class for a HashMap, which stores the hash code as part of the item,
    so that hash codes don't need to be recomputed during each resizing.

    Note that for subclasses implementing the abstract methods _bucket_getitem,
    _bucket_setitem, and _bucket_delitem, the index j 
    """
    _table: list[Optional[Item]]

    @dataclass(slots=True)
    class Item(HashMapBase.Item):
        _hash_code: int

    @abstractmethod
    def _bucket_getitem(self, j: int, k: Hashable) -> Any:
        """
        Given hash code j, search the appropriate bucket for item with key k.
        Note that hash code j can be outside the range of the array,
        and so % len(self._table) must first be applied before indexing into array.
        """
        ...

    @abstractmethod
    def _bucket_setitem(self, j: int, k: Hashable, v: Any) -> None:
        """
        Given hash code j, modify the appropriate bucket, such that key k
        becomes associated with value v.
        If there is already a corresponding value, overwrite it.
        This method is responsible for incrementing self._n.
        Also note that j is a hash code, and may be outside the range of the array,
        so % len(self._table) must first be applied.
        """
        ...

    @abstractmethod
    def _bucket_delitem(self, j: int, k: Hashable) -> None:
        """
        Given hash code j, remove item with key k from the appropriate bucket,
        or raise KeyError. Note that hash code j may be outside the range
        of the array, so % len(self._table) must first be applied.
        """
        ...

    def _hash_code(self, k: Hashable) -> int:
        """
        Generate hash code, which can be out of range of table length
        """
        return (hash(k)*self._scale + self._shift) % self._prime

    def __getitem__(self, k: Hashable) -> Any:
        j = self._hash_code(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k: Hashable, v: Any) -> None:
        j = self._hash_code(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)
    
    def __delitem__(self, k: Hashable) -> None:
        j = self._hash_code(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, new_capacity: int) -> None:
        old = self._table
        self._table = new_capacity * [None]
        self._n = 0
        for item in old:
            self._bucket_setitem(item._hash_code, item._key, item._value)