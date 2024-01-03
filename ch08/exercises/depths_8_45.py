import sys
import os
from pathlib import Path
from typing import Any

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from typing import Union
from ch08.my_practice_implementations.linked_tree import LinkedTree, Position
from ch08.exercises.tree_traversal_applications import create_organization_tree


def print_depths(tree: LinkedTree) -> None:
    def recurse_print(p: Position, depth: int) -> None:
        print(f"{p.element()}, depth {depth}")
        for c in tree.children(p):
            recurse_print(c, depth+1)
    root_pos = tree.root()
    recurse_print(root_pos, 0)



if __name__ == "__main__":
    tree = create_organization_tree()
    print_depths(tree)

