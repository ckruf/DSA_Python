from abc import abstractmethod
from typing import Optional, Iterator
from ch08.my_practice_implementations.abstract_tree import Tree, Position


class BinaryTree(Tree):
    
    @abstractmethod
    def left(self, p: Position) -> Optional[Position]:
        """
        Return the left child of the given position, or None if non-existent.
        """

    @abstractmethod
    def right(self, p: Position) -> Optional[Position]:
        """
        Return the right child of the given position, or None if non-existent.
        """

    def sibling(self, p: Position) -> Optional[Position]:
        """
        Return the sibling of the given position, or None if non-existent.
        """
        parent = self.parent(p)
        if parent is None:
            return None
        if self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p: Position) -> Iterator[Position]:
        left_child = self.left(p)
        right_child = self.right(p)
        if left_child is not None:
            yield left_child
        if right_child is not None:
            yield right_child
        