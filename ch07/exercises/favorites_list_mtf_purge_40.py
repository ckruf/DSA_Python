from dataclasses import dataclass
from typing import Any, Optional
from ch07.my_practice_implementations.positional_list import (
    PositionalList,
    Position
)


@dataclass(slots=True)
class FavoritesItem:
    _value: Any
    _access_cnt: int
    _last_access: int


class FavoritesListMTFPurge:
    """
    Favorites list 
    - keeps track of how many times items were accessed
    - implemented with move-to-front heuristic
    - purges item from list if item not accessed in last n accesses
    """
    _data: PositionalList
    _total_access_cnt: int
    _purge_cnt: int

    def __init__(self, purge_cnt: int):
        self._data = PositionalList()
        self._purge_cnt = purge_cnt
        self._total_access_cnt = 0

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return self._data.is_empty()

    def __iter__(self):
        for e in self._data:
            yield e

    def access(self, e: Any) -> None:
        """
        Access given element in list and increment its access count. 
        If the item is not in the list, add it.
        """
        if self._data.is_empty():
            walk = None
        else:
            walk = self._data.first()
        while walk is not None:
            current_favorites_item = walk.element()
            if current_favorites_item._value == e:
                current_favorites_item._access_cnt += 1
                current_favorites_item._last_access = self._total_access_cnt
                self._data.move_to_front(walk)
                break
            walk = self._data.after(walk)
        if walk is None:
            new_item = FavoritesItem(e, 1, self._total_access_cnt)
            self._data.add_first(new_item)
        last_pos = self._data.last()
        if (self._total_access_cnt - last_pos.element()._last_access) == self._purge_cnt:
            self._data.delete(last_pos)
        self._total_access_cnt += 1

    def remove(self, e: Any) -> None:
        """
        Remove given item from list, or raise Exception.
        """
        walk = self._data.first()
        while walk is not None:
            if walk.element()._value == e:
                self._data.delete(walk)
                break
            walk = self._data.after(walk)
        if walk is None:
            raise ValueError("Given element is not part of the list", e)

    def top(self, k: int):
        """
        Provide iteration of top k items by access count.
        """
        list_copy = PositionalList()
        walk = self._data.first()
        while walk is not None:
            list_copy.add_last(walk.element())
            walk = self._data.after(walk)
        for _ in range(k):
            top_item = list_copy.first()
            walk = list_copy.first()
            while walk is not None:
                if walk.element()._access_cnt > top_item.element()._access_cnt:
                    top_item = walk
                walk = list_copy.after(walk)
            yield top_item.element()
            list_copy.delete(top_item)