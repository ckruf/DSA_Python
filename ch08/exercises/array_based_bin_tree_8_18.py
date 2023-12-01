from __future__ import annotations
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from dataclasses import dataclass
from typing import Any, Optional
from ch08.my_practice_implementations import abstract_tree
from ch08.my_practice_implementations import abstract_bin_tree



@dataclass(slots=True)
class Position(abstract_tree.Position):
    _index: int
    _container: ArrayBinaryTree

    def element(self) -> Any:
        return self._container._elements[self._index]

    def __eq__(self, other) -> bool:
        return type(self) is type(other) \
        and self._container is other._container \
        and self._index is other._index


class ArrayBinaryTree(abstract_bin_tree.BinaryTree):
    _elements: list
    
    def __init__(self):
        self._elements = []

    def _make_position(self, index: int) -> Optional[Position]:
        if index >= len(self._elements):
            return None
        return Position(index, self)

    def _validate(self, p: Position) -> int:
        if not isinstance(p, Position):
            raise TypeError(f"p must be a Position instance, not {type(p)}")
        if p._container is not self:
            raise ValueError("p is not part of this tree")
        if p.element() is None:
            raise ValueError("p is no longer valid")
        return p._index
    
    def root(self) -> Optional[Position]:
        return self._make_position(0)

    def _add_root(self, e: Any) -> Position:
        if len(self._elements) > 0 and self._elements[0] is not None:
            raise ValueError("tree already has root")
        self._elements[0] = e
        return self._make_position(0)

    def left(self, p: Position) -> Optional[Position]:
        parent_index = self._validate(p)
        left_index = (2 * parent_index) + 1
        return self._make_position(left_index)

    def right(self, p: Position) -> Optional[Position]:
        parent_index = self._validate(p)
        right_index = (2 * parent_index) + 2
        return self._make_position(right_index)

    def is_leaf(self, p: Position) -> bool:
        index = self._validate(p)
        left_child_index = (2 * index) + 1
        right_child_index = (2 * index) + 2
        
        # Check if both left and right child indices are out of bounds or point to None
        left_child_exists = left_child_index < len(self._elements) and self._elements[left_child_index] is not None
        right_child_exists = right_child_index < len(self._elements) and self._elements[right_child_index] is not None

        return not left_child_exists and not right_child_exists
