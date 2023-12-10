"""
Describe how to clone a LinkedBinaryTree instance representing a proper 
binary tree, with the use of the _attach method.
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
    def _recurse_clone(subtree_root: Node) -> LinkedBinaryTree:
        sub_tree = LinkedBinaryTree()
        sub_tree._add_root(subtree_root._element)
        left_subtree = LinkedBinaryTree()
        right_subtree = LinkedBinaryTree()
        if subtree_root._left is not None:
            left_subtree = _recurse_clone(subtree_root._left)
        if subtree_root._right is not None:
            right_subtree = _recurse_clone(subtree_root._right)
        sub_tree._attach(sub_tree.root(), left_subtree, right_subtree)
        return sub_tree
    if len(bin_tree) == 0:
        return LinkedBinaryTree()
    return _recurse_clone(bin_tree.root()._node)


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