import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))


import pytest
from ch09.exercises.non_recursive_bubbling_9_30_31 import NonRecursiveHeapPQ as PriorityQueue

def test_add_and_length():
    pq = PriorityQueue()
    assert pq.is_empty() == True
    pq.add(5, 'A')
    pq.add(3, 'B')
    pq.add(7, 'C')
    assert len(pq) == 3

def test_min():
    pq = PriorityQueue()
    pq.add(5, 'A')
    pq.add(3, 'B')
    pq.add(7, 'C')
    assert pq.min() == (3, 'B')

def test_remove_min():
    pq = PriorityQueue()
    pq.add(5, 'A')
    pq.add(3, 'B')
    pq.add(7, 'C')
    assert pq.remove_min() == (3, 'B')
    assert len(pq) == 2
    assert pq.min() == (5, 'A')

def test_is_empty():
    pq = PriorityQueue()
    assert pq.is_empty() == True
    pq.add(5, 'A')
    assert pq.is_empty() == False

def test_errors():
    pq = PriorityQueue()
    with pytest.raises(Exception):
        pq.min()
    with pytest.raises(Exception):
        pq.remove_min()

def test_priority_queue_sequence_operations():
    pq = PriorityQueue()
    
    # Initially, the priority queue should be empty
    assert pq.is_empty() == True
    assert len(pq) == 0

    # Add elements
    pq.add(4, 'D')
    pq.add(1, 'A')
    pq.add(3, 'C')
    pq.add(2, 'B')
    
    # Check if the elements are added correctly
    assert not pq.is_empty()
    assert len(pq) == 4

    # Minimum should be (1, 'A') now
    assert pq.min() == (1, 'A')

    # Remove minimum and check if the min and length are updated correctly
    assert pq.remove_min() == (1, 'A')
    assert pq.min() == (2, 'B')
    assert len(pq) == 3

    # Continue removing and checking
    assert pq.remove_min() == (2, 'B')
    assert pq.min() == (3, 'C')
    assert len(pq) == 2

    # Add another element to test dynamic behavior
    pq.add(0, 'E')
    assert pq.min() == (0, 'E')
    assert len(pq) == 3

    # Remove all elements and check if the queue is empty
    pq.remove_min()
    pq.remove_min()
    pq.remove_min()
    assert pq.is_empty() == True
    assert len(pq) == 0

    # Test for exceptions on empty queue
    with pytest.raises(Exception):
        pq.min()
    with pytest.raises(Exception):
        pq.remove_min()
