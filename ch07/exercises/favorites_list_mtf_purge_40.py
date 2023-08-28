"""File containing solution attempt for exercise 7.40"""
from dataclasses import dataclass
import datetime as dt
from typing import Any, Optional
from ch07.my_practice_implementations.positional_list import PositionalList
from ch07.my_practice_implementations.linked_queue import LinkedQueue


@dataclass(slots=True)
class FavoritesItem:
    _value: Any
    _count: int
    _last_access: dt.datetime


class FavoritesListMTFPurge:
    """
    List which keeps track of how many times elements are accessed.
    Uses the move-to-front heuristic.
    Purges items which have not been accessed in the most recent n accesses
    from the list.
    """
    _purge_limit: int
    _data: PositionalList
    _access_time_stamps: LinkedQueue

    def __init__(self, purge_limit: int):
        self._purge_limit = purge_limit
        self._data = PositionalList()
        self._access_time_stamps = LinkedQueue()

    def is_empty(self) -> bool:
        return self._data.is_empty()

    def __len__(self) -> int:
        return len(self._data)

    def access(self, e: Any) -> None:
        now = dt.datetime.now(dt.timezone.utc)
        if self._data.is_empty():
            walk = None
        else:
            walk = self._data.first()
        # search for element
        while walk is not None:
            if walk.element()._value == e:
                # found, increment _count, update _last_access
                walk.element()._count += 1
                walk.element()._last_access = now
                break
            else:
                walk = self._data.after(walk)
        # element not found
        if walk is None:
            new_item = FavoritesItem(e, 1, now)
            self._data.add_first(new_item)
        else:
            self._data.move_to_front(walk)
        
        self._access_time_stamps.enqueue(now)

        if len(self._access_time_stamps) > self._purge_limit:
            cutoff = self._access_time_stamps.dequeue()    
            last_pos = self._data.last()
            if not (last_pos.element()._last_access > cutoff):
                self._data.delete(last_pos)

    def remove(self, e: Any) -> None:
        walk = self._data.first()
        while walk is not None:
            if walk.element()._value == e:
                self._data.delete(walk)
                return
            walk = self._data.after(walk)
        if walk is None:
            raise ValueError(f"element {e} is not found in list")

    def top(self, k: int):
        # make a copy of the list
        list_copy = PositionalList()
        walk = self._data.first()
        while walk is not None:
            list_copy.add_last(walk.element())
            walk = self._data.after(walk)
        # iterate over list k times, each iteration find max value and remove it
        for _ in range(k):
            walk = max = list_copy.first()
            while walk is not None:
                if walk.element()._count > max.element()._count:
                    max = walk
                walk = list_copy.after(walk)
            yield max.element()
            list_copy.delete(max)
