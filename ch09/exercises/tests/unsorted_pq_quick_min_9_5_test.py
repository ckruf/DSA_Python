import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


from ch09.exercises.unsorted_pq_quick_min_9_5 import QuickMinUnsortedPQ



def test_min_with_add():
    """
    Test the `add` method of the modified unsorted priority queue.
    Test that the minimal item updates correctly after multiple 
    `add` operations.
    """
    pq = QuickMinUnsortedPQ()
    pq.add(5, "A")
    assert pq.min() == (5, "A")
    pq.add(6, "B")
    assert pq.min() == (5, "A")
    pq.add(4, "C")
    assert pq.min() == (4, "C")


def test_min_with_remove_min():
    """
    Test the `remove_min` method of the modified unsorted priority queue.
    Test that the minimal item updates correctly after multiple
    `remove_min` operations.
    """
    pq = QuickMinUnsortedPQ()
    pq.add(5, "A")
    pq.add(4, "B")
    pq.add(3, "C")
    assert pq.min() == (3, "C")
    assert pq.remove_min() == (3, "C")
    assert pq.min() == (4, "B")
    assert pq.remove_min() == (4, "B")
    assert pq.min() == (5, "A")


def test_empty_and_fill_up():
    """
    Test that the modified priority queue correctly handles when it is completely
    emptied and filled up again.
    """
    pq = QuickMinUnsortedPQ()
    for key, value in (5, "A"), (3, "C"), (4, "B"):
        pq.add(key, value)
    for _ in range(3):
        pq.remove_min()
    pq.add(10, "Z")
    assert pq.min() == (10, "Z")
    assert pq.remove_min() == (10, "Z")


if __name__ == "__main__":
    test_min_with_remove_min()