from __future__ import annotations

from abc import abstractmethod
from typing import Sequence, Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: CT, other: CT) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)


def bin_search_recursion(left: int, right: int, values: Sequence[CT], target: CT) -> int | False:
    print(f"bin_search_recursion({left}, {right}...)")

    if len(values) == 0:
        return False

    mid = (left + right) // 2

    if values[mid] == target:
        return mid
    elif left >= right:
        return False
    elif values[mid] < target:
        return bin_search_recursion(mid + 1, right, values, target)
    else:
        return bin_search_recursion(left, mid - 1, values, target)


def bin_search(values: Sequence[CT], target: CT) -> int | False:
    """
    Wrapper of binary search for given sequence.

    :param values: sorted sequence to be searched
    :param target: queried value
    :return: index where value is found, or False
    """
    return bin_search_recursion(0, len(values) - 1, values, target)


sequence = [2, 3, 7, 10, 15, 84, 127, 489]
assert bin_search(sequence, 126) is False 