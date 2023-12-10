"""
Describe how to clone a LinkedBinaryTree instance representing a 
(not necessarily proper) binary tree, with the use of the _add_left and 
_add_right methods.
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree, Position, Node
from ch08.exercises.euler_tour_applications import create_non_positioned_bin_tree, create_binary_expression_tree

 
def clone_tree(bin_tree: LinkedBinaryTree) -> LinkedBinaryTree:
    def _recurse_clone(p_og: Position, p_clone: Position):
        og_left_child = bin_tree.left(p_og)
        og_right_child = bin_tree.right(p_og)
        if og_left_child is not None:
            cloned_left_child = cloned_tree._add_left(p_clone, og_left_child.element())
            _recurse_clone(og_left_child, cloned_left_child)
        if og_right_child is not None:
            cloned_right_child = cloned_tree._add_right(p_clone, og_right_child.element())
            _recurse_clone(og_right_child, cloned_right_child)
    
    if len(bin_tree) == 0:
        return LinkedBinaryTree()
    cloned_tree = LinkedBinaryTree()
    cloned_tree._add_root(bin_tree.root().element())
    _recurse_clone(bin_tree.root(), cloned_tree.root())
    return cloned_tree


def main() -> None:
    bin_tree = create_non_positioned_bin_tree()
    elements_before = [p.element() for p in bin_tree.inorder()]
    print("elements before:")
    print(elements_before)
    cloned_tree = clone_tree(bin_tree)
    elements_cloned = [p.element() for p in cloned_tree.inorder()]
    print("elements in cloned tree:")
    print(elements_cloned)
    elements_before = [p.element() for p in bin_tree.inorder()]
    print("elements before after cloning:")
    print(elements_before)

if __name__ == "__main__":
    main()