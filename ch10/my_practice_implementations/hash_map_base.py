import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from abc import ABC, abstractmethod
from random import randrange
from typing import Any, Hashable
from .map_base import MapBase


class HashMapBase(MapBase, ABC):
    
    def __init__(self, capacity: int = 11, p: int = 109_345_121):
        self._table = [None] * capacity
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    @abstractmethod
    def _bucket_getitem(self, j: int, k: Hashable) -> Any:
        """Search bucket j for item with key k"""
        ...

    @abstractmethod
    def _bucket_setitem(self, j: int, k: Hashable, v: Any) -> None:
        """
        Modify bucket j such that key k becomes associated with value v.
        If there is already a corresponding value, overwrite it.
        This method is responseible for incrementing self._n
        """
        ...

    @abstractmethod
    def _bucket_delitem(self, j: int, k: Hashable) -> None:
        """
        Remove item with key k from bucket j, or raise KeyError.
        """
        ...

    def __iter__(self):
        ...

    def _hash_function(self, k: Hashable) -> int:
        """
        Hash function which uses __hash__ of the key as the hash code,
        and a MAD compression function
        """
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self) -> int:
        return self._n
    
    def __getitem__(self, k: Hashable) -> Any:
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)
    
    def __setitem__(self, k: Hashable, v: Any) -> None:
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k: Hashable) -> None:
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, new_capacity: int) -> None:
        old = list(self.items())
        self._table = new_capacity * [None]
        # __setitem__ will increment back to correct size
        self._n = 0
        for k, v in old:
            self[k] = v
