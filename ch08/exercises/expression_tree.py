"""
File containing my attempts at following along with the expression tree examples.
"""

from __future__ import annotations
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from typing import Optional
from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree, \
Position



class ExpressionTree(LinkedBinaryTree):

    allowed_operators = {"/", "+", "-", "*", "x"}

    def __init__(
        self,
        token: str,
        left: Optional[ExpressionTree] = None,
        right: Optional[ExpressionTree] = None,
    ):
        super.__init__()
        if not isinstance(token, str):
            raise TypeError(
                f"token {token} must be a string, not {type(token)}"
                )
        self._add_root(token)
        if left is not None:
            if token not in self.allowed_operators:
                raise ValueError(
                    f"token must be a mathematical operator sign, not {token}"
                )
            self._attach(self.root(), left, right)

    def __str__(self) -> str:
        """Return parenthesized string representation of the tree"""
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return "".join(pieces)


    def _parenthesize_recur(self, p: Position, chars: list[str]) -> None:
        """
        Recursive function to produce an inorder list of all characters 
        of the expression.

        Call with root and empty list initially.
        List is modified in-place, not returned.
        """
        if self.is_leaf(p):
            chars.append(str(p.element()))
        else:
            chars.append("(")
            if self.left(p) is not None:
                self._parenthesize_recur(self.left(p), chars)
            chars.append(p.element())
            if self.right(p) is not None:
                self._parenthesize_recur(self.right(p), chars)
            chars.append(")")

    def evaluate(self) -> int | float:
        """Evaluate the expression represented by this tree"""


    def _evaluate_recur(self, p: Position) -> int | float:
        """
        Recursive function to evaluate the expression represented by this tree.
        Call initially with root.
        """
        if self.is_leaf(p):
            return float(p.element())
        else:
            left_result = self._evaluate_recur(self.left(p))
            right_result = self._evaluate_recur(self.right(p))
            if p.element() == "-": return left_result - right_result
            elif p.element() == "+": return left_result + right_result
            elif p.element() == "/": return left_result / right_result
            else: return left_result * right_result

    @staticmethod
    def build_expression_tree(tokens: str) -> ExpressionTree:
        """
        Build an expression tree from a string of tokens.
        This one only works for single digit numbers.
        """
        stack = []

        for char in tokens:
            # we push operators on the stack
            if char in ExpressionTree.allowed_operators:
                stack.append(char)
            # we push values as single-member expression tree on the stack
            elif char not in {"(", ")"}:
                stack.append(ExpressionTree(char))
            # if we encounter ')', we pop last three values from the stack, and
            # merge them into a new tree
            else:
                right_tree = stack.pop()
                operator = stack.pop()
                left_tree = stack.pop()
                stack.append(ExpressionTree(operator, left_tree, right_tree))
            return stack.pop()

