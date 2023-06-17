from typing import List, Any
from .positional_list import PositionalList


def insertion_sort_array_list(sequence: List[Any]) -> None:
    """
    Sort given list in place using the insertion sort algorithm.
    """
    for i in range(1, len(sequence)):
        j = i
        while j > 0 and sequence[j] < sequence[j - 1]:
            temp = sequence[j]
            sequence[j] = sequence[j - 1]
            sequence[j - 1] = temp
            j -= 1


if __name__ == "__main__":
    test_list = [9, 6, 7, 8, 1, 3, 2, 4]
    print("before sorting", test_list)
    insertion_sort_array_list(test_list)
    print("after sorting", test_list)


def insertion_sort_doubly_linked_list(sequence: PositionalList) -> None:
    """
    Sort given linked list in place using the insertion sort algorithm.
    """
    if len(sequence) < 2:
        return

    marker = sequence.first()
    while marker != sequence.last():
        pivot = sequence.after(marker)
        value = pivot.element()
        if value > marker.element():
            marker = pivot
        else:
            walk = marker
            while walk != sequence.first() and sequence.before(walk).element() > value:
                walk = sequence.before(walk)
            sequence.delete(pivot)
            sequence.add_before(walk, value)
