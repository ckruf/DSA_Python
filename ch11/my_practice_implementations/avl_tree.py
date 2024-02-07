from __future__ import annotations
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))

from dataclasses import dataclass
from typing import Optional
from .tree_map import TreeMap, Position


@dataclass(slots=True)
class Node:
    _left: Optional[Node]
    _right: Optional[Node]
    _parent: Optional[Node]
    _element: Optional[TreeMap.Item]
    _height: int = 0

    def left_height(self) -> int:
        return self._left._height if self._left is not None else 0

    def right_height(self) -> int:
        return self._right._height if self._right is not None else 0


class AVLTree(TreeMap):
    
    