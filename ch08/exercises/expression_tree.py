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

import re
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
        """
        init method, which can either create an expression tree with a single 
        element (root), or an expression tree with a root and left and right
        subtrees provided.
        """
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
        return self._evaluate_recur(self.root())


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
        Build an expression tree from an arithmetic expression string.
        """
        stack = []
        tokens = ExpressionTree.tokenize(tokens)

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

    @staticmethod
    def tokenize(expr_str: str) -> list[str]:
        """
        Helper method to tokenize an expression string, so as to ignore 
        whitespace, and handle multidigit numbers.
        """
        tokens = []
        current_number_digits = []

        for char in expr_str:
            if char.isnumeric():
                current_number_digits.append(char)
            else:
                if current_number_digits:
                    tokens.append("".join(current_number_digits))
                    current_number_digits.clear()
                if not char.isspace():
                    tokens.append(char)

        # Append the last number if present
        if current_number_digits:
            tokens.append("".join(current_number_digits))

        return tokens

    def tokenize(expr_str: str) -> list[str]:
        """
        Tokenize an expression string into brackets, operators, and numbers.
        Whitespace is ignored.
        """
        # Regex pattern: 
        # \d+ matches one or more digits (multi-digit numbers)
        # [^\w\s] matches any non-word, non-whitespace character (operators and brackets)
        pattern = r'\d+|[^\w\s]'
        return re.findall(pattern, expr_str)


if __name__ == "__main__":
    print(ExpressionTree.tokenize(" (35 + 14) + 13"))
