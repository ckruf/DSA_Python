from typing import Optional, Any
from dataclasses import dataclass
from .positional_list import PositionalList, Position



@dataclass(slots=True)
class Item:
  _element: Any
  _access_count: int


class FavoritesList:
  _data: PositionalList

  def __init__(self):
    self._data = PositionalList

  # private utilities
  def _find_in_list(self, elem: Any) -> Optional[Position]:
    walk = self._data.first()
    while walk != self._data.last() and self._data.after(walk).element()._element != elem:
      walk = self._data.after(walk)
    return self._data.after(walk)


  def _move_up(self, p: Position) -> None:
    pass

  # public API
  def access(self, elem: Any) -> None:
    """
    'Access' the given element.
    If it exists in the list, increment its access count.
    If it doesn't exist, add it to the list.
    """

  def remove(self, elem: Any) -> None:
    """Remove the given element from the list"""

  def top(self, k: int) -> None:
    """Generate a sequence of top k elements in the list (yield)"""

  def __len__(self) -> int:
    return len(self._data)
  
  def is_empty(self) -> bool:
    return self._data.is_empty()
  
