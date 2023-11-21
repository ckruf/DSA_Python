"""
File containing re-implementation of tree traversal applications, using Euler Tour.
- unindented table of contents
- indented table of contents
- indented and labelled/numbered table of contents
- parenthetic tree representation
- directory size computation
- directory size computation with indented printing out
"""

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from dataclasses import dataclass
from typing import Any, Optional
from ch08.my_practice_implementations.euler_tour import EulerTour, BinaryEulerTour
from ch08.exercises.tree_traversal_applications import create_document_tree, create_organization_tree
from ch08.my_practice_implementations.linked_tree import Position
from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree


class UnindentedPrintTour(EulerTour):

    def _hook_previsit(self, p: Position, d: int, path: list[int]) -> None:
        print(p.element())


class IndentedPrintTour(EulerTour):

    def _hook_previsit(self, p: Position, d: int, path: list[int]) -> None:
        print(2 * d * " " + p.element())


class NumberedIndentedPrintTour(EulerTour):

    def _hook_previsit(self, p: Position, d: int, path: list[int]) -> None:
        indent = 2 * d * " "
        label = ".".join(str(j + 1) for j in path)
        print(indent + " " + label + " " + p.element())


class ParentheticPrintTour(EulerTour):

    def _hook_previsit(self, p: Position, d: int, path: list[int]) -> None:
        if path and path[-1] == 0:
            print("(", end="")
        print(p.element(), end="")

    def _hook_postvisit(self, p: Position, d: int, path: list[int], results: list) -> Any:
        if path and path[-1] + 1 == self.tree().num_children(self.tree().parent(p)):
            print(")", end="")
        else:
            if path:
                print(",", end="")


class FilesizeComputingTour(EulerTour):

    def _hook_postvisit(self, p: Position, d: int, path: list[int], results: list) -> Any:
        return p.element().space() + sum(results)
    

@dataclass(slots=True)
class PositionedItem:

    element: Any
    X: Optional[int] = None
    Y: Optional[int] = None

    def set_X(self, X: int) -> None:
        self.X = X

    def set_Y(self, Y: int) -> None:
        self.Y = Y


def create_binary_tree() -> LinkedBinaryTree:
    bin_tree = LinkedBinaryTree()
    root_pos = bin_tree._add_root(PositionedItem("H"))
    F_pos = bin_tree._add_left(root_pos, PositionedItem("F"))
    B_pos = bin_tree._add_left(F_pos, PositionedItem("B"))
    bin_tree._add_left(B_pos, PositionedItem("A"))
    D_pos = bin_tree._add_right(B_pos, PositionedItem("D"))
    bin_tree._add_left(D_pos, PositionedItem("C"))
    bin_tree._add_right(D_pos, PositionedItem("E"))
    bin_tree._add_right(F_pos, PositionedItem("G"))
    L_pos = bin_tree._add_right(root_pos, PositionedItem("L"))
    J_pos = bin_tree._add_left(L_pos, PositionedItem("J"))
    bin_tree._add_left(J_pos, PositionedItem("I"))
    bin_tree._add_right(J_pos, PositionedItem("K"))
    bin_tree._add_right(L_pos, PositionedItem("M"))
    return bin_tree






class BinaryLayoutTour(BinaryEulerTour):
    _count: int
    
    def __init__(self, tree: LinkedBinaryTree):
        super().__init__(tree)
        self._count = 0

    def _hook_invisit(self, p: Position, d: int, path: list[int]) -> None:
        p.element().set_X(self._count)
        p.element().set_Y(d)
        self._count += 1
          

def print_unindented() -> None:
    document_tree = create_document_tree()
    unindented_tour = UnindentedPrintTour(document_tree)
    unindented_tour.execute()


def print_indented() -> None:
    document_tree = create_document_tree()
    indented_tour = IndentedPrintTour(document_tree)
    indented_tour.execute()


def print_numbered_and_indented() -> None:
    org_tree = create_organization_tree()
    indented_numbered_tour = NumberedIndentedPrintTour(org_tree)
    indented_numbered_tour.execute()


def print_parenthetic() -> None:
    org_tree = create_organization_tree()
    parenthetic_tour = ParentheticPrintTour(org_tree)
    parenthetic_tour.execute()


def set_coordinates() -> None:
    bin_tree = create_binary_tree()
    coordinate_tour = BinaryLayoutTour(bin_tree)
    coordinate_tour.execute()
    for p in bin_tree.positions():
        print(p.element())


if __name__ == "__main__":
    set_coordinates()