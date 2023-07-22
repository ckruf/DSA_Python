from typing import Optional, Any
from dataclasses import dataclass

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.absolute()
sys.path.insert(0, str(src_dir))

from my_practice_implementations.positional_list import PositionalList, Position


@dataclass(slots=True)
class Item:
    _element: Any
    _access_count: int


class FavoritesList:
    """
    Favorites list implemented using PositionalList. 
    A favorites list allows us to access and remove items, and provides a 
    method for viewing the top k accessed items.
    """
    _data: PositionalList[Item]

    def __init__(self):
        self._data = PositionalList()

    # private utilities
    def _find_in_list(self, elem: Any) -> Optional[Position[Item]]:
        if len(self._data) == 0:
            return None
        walk = self._data.first()
        while walk is not None and walk.element()._element != elem:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p: Position[Item]) -> None:
        if p == self._data.first():
            return
        access_cnt = p.element()._access_count
        # IMPORTANT!!!
        # walk must be initialized to 'before' position, otherwise, on the final]
        # line, we would be adding an item before a position which we have
        # deleted, leading to error
        walk = self._data.before(p)
        # IMPORTANT!!!
        # must include this check, otherwise we could move position even when
        # it should not be moved
        if access_cnt <= walk.element()._access_count:
            return
        while (
            walk != self._data.first()
            and access_cnt > self._data.before(walk).element()._access_count
        ):
            walk = self._data.before(walk)

        self._data.add_before(walk, self._data.delete(p))

    # public API
    def access(self, elem: Any) -> None:
        """
        'Access' the given element.
        If it exists in the list, increment its access count.
        If it doesn't exist, add it to the list.
        """
        elem_position = self._find_in_list(elem)
        if elem_position:
            elem_position.element()._access_count += 1
            self._move_up(elem_position)
        else:
            self._data.add_last(Item(elem, 1))

    def remove(self, elem: Any) -> None:
        """Remove the given element from the list"""
        elem_position = self._find_in_list(elem)
        if elem_position is not None:
            self._data.delete(elem_position)

    def top(self, k: int) -> None:
        """Generate a sequence of top k elements in the list (yield)"""
        length = len(self._data)
        if not 0 < k <= length:
            raise ValueError(f"k must be greater than 0 and less than {length + 1}")
        walk = self._data.first()
        counter = 0
        while counter < k:
            yield walk.element()._element
            walk = self._data.after(walk)
            counter += 1

    def clear(self) -> None:
        """
        Exercise 7.22 - clearing the list.
        """
        self._data = PositionalList()

    def reset_counts(self) -> None:
        """
        Exercise 7.23 - resetting all access counts to 0.
        """
        for item in self._data:
            item._access_count = 0

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return self._data.is_empty()
