"""
File containing an implementation of a Euler tour, where each position in a tree 
is visited twice, once before its subtree is toured, and once after.
"""

from typing import Any
from ch08.my_practice_implementations.linked_tree import LinkedTree, Position
from ch08.my_practice_implementations.linked_binary_tree import LinkedBinaryTree

class EulerTour:

    _tree: LinkedTree

    def __init__(self, tree: LinkedTree):
        self._tree = tree

    def tree(self) -> LinkedTree:
        return self._tree
    
    def execute(self) -> Any:
        """Perform the tour and return any result from post visit of root"""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p: Position, d: int, path: list[int]) -> Any:
        """
        Perform a Euler tour of subtree routed at position p.

        :param p: root of (sub)tree from which to start the tour
        :param d: depth of p in the tree
        :param path: list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p: Position, d: int, path: list[int]) -> None:
        pass
    
    def _hook_postvisit(self, p: Position, d: int, path: list[int], results: list) -> Any:
        pass


class BinaryEulerTour(EulerTour):

    _tree: LinkedBinaryTree

    def __init__(self, tree: LinkedBinaryTree):
        self._tree = tree

    def tree(self) -> LinkedBinaryTree:
        return self._tree

    def _tour(self, p: Position, d: int, path: list[int]) -> Any:
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        
        self._hook_invisit(p, d, path)
        
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()

        answer = self._hook_postvisit(p, d, path, results)
        
        return answer

    def _hook_invisit(self, p: Position, d: int, path: list[int]) -> None:
        pass
