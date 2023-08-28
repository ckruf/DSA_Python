from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
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

    