import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from typing import Union, Iterable
from ch09.my_practice_implementations.sorted_priority_queue import SortedPriorityQueue
from ch09.my_practice_implementations.unsorted_priority_queue import UnsortedPriorityQueue
from ch09.my_practice_implementations.heap import HeapPriorityQueue

PQ = Union[SortedPriorityQueue, UnsortedPriorityQueue, HeapPriorityQueue]


def pq_sort(elements: Iterable) -> list:
    n = len(elements)
    p_q = HeapPriorityQueue()
    sorted_elements = []
    for j in range(n):
        element = elements[j]
        p_q.add(element, element)
    for j in range(n):
        k, v = p_q.remove_min()
        sorted_elements.append(v)


def selection_sort(elements: list) -> None:
    for i in range(len(elements)):
        min_index = i
        for j in range(i, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j
        elements[i], elements[min_index] = elements[min_index], elements[i]


def insertion_sort(elements: list) -> None:
    for i in range(1, len(elements)):
        j = i
        while elements[j] < elements[j-1] and j > 0:
            elements[j], elements[j-1] = elements[j-1], elements[j]
            j -= 1


if __name__ == "__main__":
    elements = [17, 11, 25, 19, 27, 10]
    selection_sort(elements)
    print(elements)
    elements = [17, 11, 25, 19, 27, 10]
    insertion_sort(elements)
    print(elements)
