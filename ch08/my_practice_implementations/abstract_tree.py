from abc import ABCMeta, abstractmethod
from collections import deque
from typing import Any, Optional, Iterator


class Position(metaclass=ABCMeta):

    @abstractmethod
    def element(self) -> Any:
        ...

    @abstractmethod
    def __eq__(self, other) -> bool:
        ...

    def __ne__(self, other) -> bool:
        return not (self == other)


class Tree(metaclass=ABCMeta):

    @abstractmethod
    def root(self):
        ...

    @abstractmethod
    def parent(self, p: Position) -> Optional[Position]:
        pass

    @abstractmethod
    def num_children(self, p: Position) -> int:
        ...

    @abstractmethod
    def children(self, p: Position) -> Iterator[Position]:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...

    def is_root(self, p: Position) -> bool:
        return p == self.root()

    def is_leaf(self, p: Position) -> bool:
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        return len(self) == 0

    def height(self, p: Optional[Position] = None) -> int:
        """Compute height of given position, or entire tree"""
        if p is None:
            p = self.root()
        if self.is_leaf():
            return 0
        else:
            return 1 + max(self.height(child) for child in self.children(p))

    def depth(self, p: Position) -> int:
        """Compute depth of given position"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def preorder(self) -> Iterator[Position]:
        """Generate preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p: Position) -> Iterator[Position]:
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def _subtree_preorder_simple(self, p: Position) -> Iterator[Position]:
        yield p
        for c in self.children():
            yield from self._subtree_preorder_simple(c)

    def postorder(self) -> Iterator[Position]:
        """Generate postorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
        
    def _subtree_postorder(self, p: Position) -> Iterator[Position]:
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def _subtree_postorder_simple(self, p: Position) -> Iterator[Position]:
        for c in self.children(p):
            yield from self._subtree_postorder_simple(c)
        yield p

    def breadthfirst(self) -> Iterator[Position]:
        if self.is_empty():
            return
        Q = deque()
        Q.append(self.root())
        while Q:
            p = Q.popleft()
            yield p
            for c in self.children(p):
                Q.append(c)

    def positions(self) -> Iterator[Position]:
        """Generate an iteration of all positions in the tree"""
        return self.preorder()

    
    def __iter__(self) -> Iterator[Any]:
        """Generate an iteration of all elements in the tree"""
        for p in self.positions():
            yield p.element()
