from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Item:
    _key: int
    _value: Any

    def __lt__(self, other: Item) -> bool:
        assert type(other) is type(self)
        return self._key < other._key

    def to_tuple(self) -> tuple[int, Any]:
        return self._key, self._value


class PriorityQueueBase:
    
    def is_empty(self) -> bool:
        return len(self) == 0