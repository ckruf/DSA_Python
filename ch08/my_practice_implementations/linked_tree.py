from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional
from ch08.my_practice_implementations import abstract_tree


@dataclass(slots=True)
class Node:
    _element: Any
    _parent: Optional[Node]
    _children: Optional[List[Node]]


@dataclass(slots=True)
class Position(abstract_tree.Position):
    _node: Optional[Node]
    _container: LinkedTree

    def element(self) -> Any:
        return self._node._element

    def __eq__(self, other) -> bool:
        return type(self) is type(other) and self._node is other._node


class LinkedTree(abstract_tree.Tree):
    pass