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


class SplayTreeMap(TreeMap):

    def _splay(self, p: Position) -> None:
        parent = self.parent(p)
        grandparent = self.parent(parent)
        if grandparent is None:
            # zig case
            self._rotate(p)
        elif (self.left(grandparent) == parent) == (self.left(parent) == p):
            # zig zig case
            self._rotate(parent)
            self._rotate(p)
        else:
            # zig zag case
            self._rotate(p)
            self._rotate(p)

    def _rebalance_access(self, p: Position):
        self._splay(p)

    def _rebalance_delete(self, p: Position):
        self._splay(p)

    def _rebalance_insert(self, p: Position):
        self._splay(p)

    