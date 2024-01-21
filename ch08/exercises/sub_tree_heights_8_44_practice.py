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
from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree, Position, Node
from ch08.my_practice_implementations.linked_tree import LinkedTree
from ch08.exercises.euler_tour_applications import create_non_positioned_bin_tree, create_binary_expression_tree
from ch08.exercises.tree_traversal_applications import create_organization_tree, create_modified_organization_tree
from ch08.my_practice_implementations.euler_tour import EulerTour


def print_subtree_heights(tree: Union[LinkedTree, LinkedBinaryTree]):
    def _recurse(p: Position, d: int):
        greatest_depth = d
        for c in tree.children(p):
            subtree_depth = _recurse(c, d+1)
            if subtree_depth > greatest_depth:
                greatest_depth = subtree_depth
        subtree_heigth = greatest_depth - d
        print(f"height of subtree at {p.element()} is {subtree_heigth}")
        return greatest_depth
    if not tree.is_empty():
        _recurse(tree.root(), 0)


if __name__ == "__main__":
    tree = create_organization_tree()
    print_subtree_heights(tree)