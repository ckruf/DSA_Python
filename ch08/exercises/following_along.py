"""
File containing my attempts at examples in this chapter (not exercises).
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from ch08.my_practice_implementations.linked_tree import LinkedTree, Position


def create_document_tree() -> LinkedTree:
    """
    Create the tree from Figure 8.15, representing the hierarchical structure
    of a document.
    """
    document_tree = LinkedTree()
    root_pos = document_tree.add_root("Paper")
    
    document_tree.add_child(root_pos, "Title")
    document_tree.add_child(root_pos, "Abstract")
    
    first_section_pos = document_tree.add_child(root_pos, "§1")
    document_tree.add_child(first_section_pos, "§1.1")
    document_tree.add_child(first_section_pos, "§1.2")

    second_section_pos = document_tree.add_child(root_pos, "§2")
    document_tree.add_child(second_section_pos, "§2.1")
    document_tree.add_child(second_section_pos, "§2.2")
    document_tree.add_child(second_section_pos, "§2.3")

    third_section_pos = document_tree.add_child(root_pos, "§3")
    document_tree.add_child(third_section_pos, "§3.1")
    document_tree.add_child(third_section_pos, "§3.2")

    document_tree.add_child(root_pos, "References")

    return document_tree


def unindented_table_of_contents(document_tree: LinkedTree) -> None:
    """
    Given a tree, representing the hierarchical structure of a document,
    print an unindented table of contents for the document.
    """
    for p in document_tree.preorder():
        print(p.element())


def indented_table_of_contents(document_tree: LinkedTree, p: Position, depth: int) -> None:
    pass


if __name__ == "__main__":
    document_tree = create_document_tree()
    unindented_table_of_contents(document_tree)
