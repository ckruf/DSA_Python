from collections.abc import MutableMapping
from dataclasses import dataclass
from typing import Any


class MapBase(MutableMapping):

    @dataclass(slots=True)
    class Item:
        _key: Any
        _value: Any

        def __eq__(self, other) -> bool:
            return type(self) is type(other) and self._key == other._key
        
        def __ne__(self, other):
            return not (self == other)
        
        def __lt__(self, other):
            assert type(self) is type(other)
            return self._key < other._key
         