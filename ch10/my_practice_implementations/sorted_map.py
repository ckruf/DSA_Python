import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from typing import Any, Optional
from .map_base import MapBase


OPTIONAL_KV = Optional[tuple[Any, Any]]


class SortedTableMap(MapBase):
    """
    Table map implemented using sorted list.
    Search/read operations are O(log(n)), thanks to binary search.
    Updates of existing key values are also O(log(n)).
    Insertion of new key/value pairs and deletions are O(n) in the worst
    case, because inserts and deletions in a list are O(n) in the worst case,
    due to the need to shift subsequent items.
    """
    _table: list[MapBase.Item]

    def __init__(self):
        self._table = []

    def _find_index(self, k: int, low: int, high: int) -> int:
        """
        Inexact binary search implementation.
        Given key k, return either the index of the position at which k is found,
        or the index of the smallest item greater than k (just to the right of k).
        Note that in case that k is not present in the table, and k is greater
        than any present key, the returned index will be out of bounds.  
        """
        if low > high:
            return high + 1
        mid = low + high // 2
        if self._table[mid]._key == k:
            return mid
        elif self._table[mid]._key > k:
            return self._find_index(k, low, mid - 1)
        else:
            return self._find_index(k, mid+1, high)

    def __len__(self) -> int:
        return len(self._table)

    def __getitem__(self, k: Any) -> Any:
        table_length = len(self._table)
        index = self._find_index(k, 0, table_length - 1)
        if index == table_length:
            raise KeyError("Key error: " + repr(k))
        item = self._table[index]
        if item._key == k:
            return item._value
        raise KeyError("Key error: " + repr(k))

    def __setitem__(self, k: Any, v: Any) -> None:
        table_length = len(self._table)
        index = self._find_index(k, 0, table_length - 1)
        if index == table_length:
            self._table.append(self.Item(k, v))
        elif self._table[index]._key == k:
            self._table[index]._value = v
        else:
            self._table.insert(index, self.Item(k, v))

    def __delitem__(self, k : Any) -> None:
        table_length = len(self._table)
        index = self._find_index(k, 0, table_length - 1)
        if index == table_length or self._table[index]._key != k:
            raise KeyError("Key error: " + repr(k))
        self._table.pop(index)

    def __iter__(self):
        """Produce an iteration of keys from minimum to maximum"""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Produce an iteration of keys from maximum to minimum"""
        for item in reversed(self._table):
            yield item._key

    def find_min(self) -> OPTIONAL_KV:
        """Return the item with the minimum key and its corresponding value"""
        if len(self._table) == 0:
            return None
        min_item = self._table[0]
        return min_item._key, min_item._value

    def find_max(self) -> OPTIONAL_KV:
        """Return the item with the maximum key and its corresponding value"""
        if len(self._table) == 0:
            return None
        max_item = self._table[-1]
        return max_item._key, max_item._value

    def find_ge(self, k: Any) -> OPTIONAL_KV:
        """
        Given a key, return the least key greater than or equal to the given key, 
        and its corresponding value
        """
        table_len = len(self._table)
        index = self._find_index(k, 0, table_len - 1)
        if index == table_len:
            return None
        ge_item = self._table[index]
        return ge_item._key, ge_item._value

    def find_gt(self, k: Any) -> OPTIONAL_KV:
        """
        Given a key, return the least key greater than the given key,
        and its corresponding value
        """
        table_len = len(self._table)
        index = self._find_index(k, 0, table_len - 1)
        if index == table_len:
            return None
        ge_item = self._table[index]
        if ge_item._key > k:
            return ge_item._key, ge_item._value
        # key is equal
        if index == table_len - 1:
            return None
        return self._table[index + 1]._key, self._table[index + 1]._value

    def find_le(self, k: Any) -> OPTIONAL_KV:
        """
        Given a key, return the greatest key less or equal to the
        given key, and its corresponding value
        """
        table_len = len(self._table)
        index = self._find_index(k, 0, table_len - 1)
        if index == table_len:
            return self._table[index - 1]._key, self._table[index - 1]._value
        if self._table[index]._key == k:
            return self._table[index]._key, self._table[index]._value
        if index == 0:
            return None
        return self._table[index - 1]._key, self._table[index - 1]._value

    def find_lt(self, k: Any) -> OPTIONAL_KV:
        """
        Given a key, return the greatest key less than the given key,
        and its corresponding value
        """
        table_len = len(self._table)
        index = self._find_index(k, 0, table_len - 1)
        if index == 0:
            return None
        return self._table[index - 1]._key, self._table[index - 1]._value

    def find_range(
        self,
        start: Optional[int] = None,
        stop: Optional[int] = None
    ):
        """
        Produce an iteration of keys in the range start <= k < stop.
        If start is None, start with minimum value.
        If stop is None, end with maximum value.
        """
        if start is None:
            start_index = 0
        table_len = len(self._table)
        start_index = self._find_index(start, 0, table_len)
        if stop is None:
            stop_index = table_len
        stop = self._find_index(start, 0, table_len)
        for i in range(start_index, stop_index):
            yield self._table[i]._key