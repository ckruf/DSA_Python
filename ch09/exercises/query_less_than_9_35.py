import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))

from ch09.my_practice_implementations.heap import HeapPriorityQueue, Item


def test_heap() -> HeapPriorityQueue:
    """
    Construct the heap from figure 9.12a p397 in Goodrich.
    """
    elements = [
        (2, "B"),
        (5, "A"), (4, "C"),
        (15, "K"), (9, "F"), (7, "Q"), (6, "Z"),
        (16, "X"), (25, "J"), (14, "E"), (12, "H"), (11, "S"), (8, "W"), (20, "B"), (10, "L")
    ]
    heap = HeapPriorityQueue(elements)
    return heap

def find_items_less_than_or_equal_to(heap: HeapPriorityQueue, key: int) -> list[Item]:
    """
    Given a heap, and a key, find all the items in the heap whose key is
    less than or equal to the given key.
    """
    def _recurse(position_index: int, results: list[int]):
        item = heap._data[position_index]
        if item._key <= key:
            results.append(position_index)
        if heap._has_left(position_index):
            _recurse(heap._left(position_index), results)
        if heap._has_right(position_index):
            _recurse(heap._right(position_index), results)
    
    item_indices = []
    if len(heap) > 0:
        _recurse(0, item_indices)
    return list(map(lambda x: heap._data[x], item_indices))


if __name__ == "__main__":
    heap = test_heap()
    print(find_items_less_than_or_equal_to(heap, 7))