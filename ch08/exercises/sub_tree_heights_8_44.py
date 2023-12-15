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


def subtree_heights(tree: Union[LinkedTree, LinkedBinaryTree]) -> int:

    def _recurse_height(
            p: Position,
            current_depth: int,
        ) -> int:
        """
        The challenge in this problem lies in the fact that we need to keep track
        of two different heights/depths. First of all, we need to keep track
        of the height of the subtree of any given node. We can do this by

        :param p: the position currently being processed
        :param current_depth: the depth of the current position
        :param greatest_child_depth: the maximum depth seen when traversing subtree
        """
        subtree_depth = current_depth
        for c in tree.children(p):
            single_child_depth = _recurse_height(c, current_depth+1, )
            if single_child_depth > subtree_depth:
                subtree_depth = single_child_depth

        print(f"position={p.element()}, current_depth={current_depth}, subtree_depth={subtree_depth}")
        return subtree_depth
        
    _recurse_height(tree.root(), 0,)



if __name__ == "__main__":
    org_tree = create_modified_organization_tree()
    subtree_heights(org_tree)
    