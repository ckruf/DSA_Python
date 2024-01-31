import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))


from time import perf_counter_ns
from typing import Any, Hashable, Optional, Union
from ch10.my_practice_implementations.load_control_hash_map_base import LoadControlHashMapBase
from ch10.my_practice_implementations.unsorted_table_map import UnsortedTableMap


class LoadControlChainHashMap(LoadControlHashMapBase):
    _table: list[Optional[UnsortedTableMap]]

    def __init__(self, capacity: int = 11, p: int = 109345121, load_factor: float = 0.5):
        self.collision_counter = 0
        super().__init__(capacity, p, load_factor)
    
    def _bucket_getitem(self, j: int, k: Hashable) -> Any:
        if self._table[j] is None:
            raise KeyError()
        linear_map = self._table[j]
        return linear_map[k]
    
    def _bucket_setitem(self, j: int, k: Hashable, v: Any) -> None:
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        else:
            self.collision_counter += 1
        linear_map = self._table[j]
        original_size = len(linear_map)
        linear_map[k] = v
        if len(linear_map) > original_size:
            self._n += 1


    def _bucket_delitem(self, j: int, k: Hashable) -> None:
        if self._table[j] is None:
            raise KeyError()
        del self._table[j][k]

    def __iter__(self):
        for i in range(len(self._table)):
            if self._table[i] is not None:
                for key in self._table[i]:
                    yield key

    

class LoadControlLinearProbeHashmap(LoadControlHashMapBase):
    _AVAIL = object()
    _table: list[Union[LoadControlChainHashMap.Item, None]]

    def __init__(self, capacity: int = 11, p: int = 109345121, load_factor: float = 0.5):
        self.collision_counter = 0
        super().__init__(capacity, p, load_factor)

    
    def _is_available(self, index) -> bool:
        return self._table[index] == self._AVAIL or self._table[index] is None
    
    def _find_slot(self, j: int, k: Hashable) -> tuple[bool, int]:
        """
        Try to find key k at index j, using linear probing.
        If found, return True, index where found
        Else, return False, index of first available slot
        """
        first_available = None
        while True:
            if self._is_available(j):
                if first_available is None:
                    first_available = j
                if self._table[j] is None:
                    return False, first_available
            elif self._table[j]._key == k:
                return True, j
            else:
                self.collision_counter += 1
            j = (j + 1) % len(self._table)

    
    def _bucket_getitem(self, j: int, k: Hashable) -> Any:
        found, index = self._find_slot(j, k)
        if found:
            return self._table[index]._value
        raise KeyError()
    
    def _bucket_setitem(self, j: int, k: Hashable, v: Any) -> None:
        found, index = self._find_slot(j, k)
        # overwrite existing
        if found:
            self._table[index]._value = v
        # create new
        else:
            self._table[index] = self.Item(k, v)
            self._n += 1

    def _bucket_delitem(self, j: int, k: Hashable) -> None:
        found, index = self._find_slot(j, k)
        if found:
            self._table[index] = self._AVAIL
        else:
            raise KeyError()
        
    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key


MapType = Union[LoadControlChainHashMap, LoadControlLinearProbeHashmap]


def load_words_file() -> list[str]:
    with open("./ch10/words", "r") as file:
        lines = [line.strip() for line in file]
    return lines


def fill_map(map: MapType, keys: list[str]) -> int:
    """
    Load words from file containing 10,000 words into the given map, and 
    return the time that it took.
    """
    start_time = perf_counter_ns()
    for key in keys:
        map[key] = None
    end_time = perf_counter_ns()
    elapsed_time = end_time - start_time
    return elapsed_time




def run_experiment() -> None:
    load_factors = [0.1, 0.3, 0.5, 0.7, 0.9]
    words = load_words_file()
    for factor in load_factors:
        chain_map = LoadControlChainHashMap(load_factor=factor)
        probe_map = LoadControlLinearProbeHashmap(load_factor=factor)
        chain_map_time = fill_map(chain_map, words)
        probe_map_time = fill_map(probe_map, words)
        print(f"Chain map with load factor {factor} took {chain_map_time:,} ns to load all words, with {chain_map.collision_counter} collisions")
        print(f"Probe map with load factor {factor} took {probe_map_time:,} ns to load all words with {probe_map.collision_counter} collisions")



if __name__ == "__main__":
    run_experiment()