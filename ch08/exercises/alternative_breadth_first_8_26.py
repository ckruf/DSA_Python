import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from collections import deque
from typing import Iterator
from ch08.my_practice_implementations.abstract_tree import Tree, Position


class AltTree(Tree):

    def breadthfirst(self) -> Iterator[Position]:
        if self.is_empty():
            return
        Q = deque()
        Q.append(self.root())
        while Q:
            p = Q.popleft()
            yield p
            Q.extend(self.children(p))
