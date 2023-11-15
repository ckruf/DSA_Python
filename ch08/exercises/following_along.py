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


def create_organization_tree() -> LinkedTree:
    """
    Create the tree from Figure 8.2, represeneting the organizational
    structure of a fictitious corporation.
    """
    organization_tree = LinkedTree()
    root_pos = organization_tree.add_root("Electronics R' Us")

    organization_tree.add_child(root_pos, "R&D")
    sales_pos = organization_tree.add_child(root_pos, "Sales")

    organization_tree.add_child(sales_pos, "Domestic")
    international_pos = organization_tree.add_child(sales_pos, "International")
    
    organization_tree.add_child(international_pos, "Canada")
    organization_tree.add_child(international_pos, "S. America")
    overseas_pos = organization_tree.add_child(international_pos, "Overseas")

    organization_tree.add_child(overseas_pos, "Africa")
    organization_tree.add_child(overseas_pos, "Europe")
    organization_tree.add_child(overseas_pos, "Asia")
    organization_tree.add_child(overseas_pos, "Australia")

    organization_tree.add_child(root_pos, "Purchasing")
    manufacturing_pos = organization_tree.add_child(root_pos, "Manufacturing")

    organization_tree.add_child(manufacturing_pos, "TV")
    organization_tree.add_child(manufacturing_pos, "CD")
    organization_tree.add_child(manufacturing_pos, "Tuner")

    return organization_tree


def unindented_table_of_contents(document_tree: LinkedTree) -> None:
    """
    Given a tree, representing the hierarchical structure of a document,
    print an unindented table of contents for the document.
    """
    for p in document_tree.preorder():
        print(p.element())


def indented_table_of_contents(
    document_tree: LinkedTree, 
    p: Position,
    depth: int,
) -> None:
    """
    Given a tree, representing the hierarchical structure of a document, 
    print and indented table of contents for the document.
    Initially call with root as the position, and 0 as the depth.
    """
    print(2* depth * " " + p.element())
    for c in document_tree.children(p):
        indented_table_of_contents(document_tree, c, depth + 1)


def indented_numbered_tree_print(
    document_tree: LinkedTree,
    p: Position,
    depth: int,
    path: list[int]
) -> None:
    """
    Given a tree, print out the tree with indentation and numbering.
    Children should be labelled sequentially, and each level should
    have a dot and be labelled again.
    For example:
    root
      1 first child
      2 second_child
        2.1 first child of second child
        2.2 second child of second child
      3. third child
    Call initially with root, 0 , empty list
    """
    label = ".".join(str(j) for j in path)
    print(2 * depth * " " + label, p.element())
    path.append(1)
    for c in document_tree.children(p):
        indented_numbered_tree_print(document_tree, c, depth + 1, path)
        path[-1] += 1
    path.pop()


if __name__ == "__main__":
    document_tree = create_document_tree()
    unindented_table_of_contents(document_tree)
    indented_table_of_contents(document_tree, document_tree.root(), 0)
    organization_tree = create_organization_tree()
    indented_numbered_tree_print(organization_tree, organization_tree.root(), 0, [])
