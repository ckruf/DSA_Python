import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))

from math import ceil
from typing import Hashable, Any
from .hash_map_base import HashMapBase
from ch10.exercises.prime_sieve_10_31 import prime_in_range



class LoadControlHashMapBase(HashMapBase):
    """
    Base class for a hash map, which allows the user to set the
    maximum load factor the underlying array can reach before being resized.
    """

    def __init__(
        self,
        capacity: int = 11,
        p: int = 109345121,
        load_factor: float = 0.5
    ):
        super().__init__(capacity, p)
        self._load_factor = load_factor

    def __setitem__(self, k: Hashable, v: Any) -> None:
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n / len(self._table) > self._load_factor:
            new_size = ceil(len(self._table) / self._load_factor)
            self._resize(new_size)