"""File containing solution attempt for exercise 7.39"""
from ch07.my_practice_implementations.positional_list import (
    PositionalList,
    Position
)
from typing import Any, Optional


class PositionalQueue:
    _data: PositionalList

    def __init__(self):
        self._data = PositionalList()

    # utilities 
    def __len__(self) -> int:
        return len(self._data)
    
    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __iter__(self):
        for e in self._data:
            yield e
    
    # accessors 
    def first(self) -> Position:
        if len(self._data) == 0:
            raise Exception("Queue is empty")
        return self._data.first()
    
    def last(self) -> Position:
        if len(self._data) == 0:
            raise Exception("Queue is empty")
        return self._data.last()
    
    def after(self, p: Position) -> Optional[Position]:
        return self._data.after(p)
    
    def before(self, p: Position) -> Optional[Position]:
        return self._data.before(p)

    # modifiers 
    def enqueue(self, e: Any) -> Position:
        return self._data.add_last(e)
    
    def dequeue(self) -> Any:
        if len(self._data) == 0:
            raise Exception("Can't dequeue from empty queue")
        return self._data.delete(self._data.first())
    
    def delete(self, p: Position) -> Any:
        return self._data.delete(p)