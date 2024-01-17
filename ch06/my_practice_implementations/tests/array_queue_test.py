import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

import pytest
from ch06.my_practice_implementations.revisited_array_queue import ArrayQueue, Empty


def test_enqueue_dequeue_no_resize():
    q = ArrayQueue()
    elems = ["A", "B", "C", "D", "E"]
    for e in elems:
        q.enqueue(e)
    for e in elems:
        assert e == q.dequeue()


def test_length():
    q = ArrayQueue()
    elems = ["A", "B", "C", "D", "E"]
    for e in elems:
        q.enqueue(e)
    assert len(q) == len(elems)
    while not q.is_empty():
        q.dequeue()
    assert len(q) == 0


def test_resize():
    q = ArrayQueue()
    elems = ["A", "B", "C" ,"D", "E"]
    for e in elems:
        q.enqueue(e)
    q._resize(30)
    for e in elems:
        assert q.dequeue() == e


def test_enqueue_dequeue_many():
    q = ArrayQueue()
    for i in range(100):
        q.enqueue(i)
    for i in range(50):
        assert q.dequeue() == i
    for i in range(10):
        q.enqueue(i)
    for i in range(50):
        assert q.dequeue() == i + 50
    for i in range(30):
        q.enqueue(i)
    for i in range(10):
        assert q.dequeue() == i



def test_empty_queue_exception():
    q = ArrayQueue()
    with pytest.raises(Empty):
        q.dequeue()
    with pytest.raises(Empty):
        q.first()

def test_queue_capacity_reduction():
    q = ArrayQueue()
    for i in range(8):
        q.enqueue(i)
    for i in range(7):
        q.dequeue()
    assert len(q._data) < ArrayQueue.INITIAL_SIZE

def test_resize_value_error():
    q = ArrayQueue()
    for i in range(5):
        q.enqueue(i)
    with pytest.raises(ValueError):
        q._resize(3)

def test_first_element():
    q = ArrayQueue()
    q.enqueue('X')
    assert q.first() == 'X'
    assert len(q) == 1  # Ensure the item is not removed

def test_enqueue_dequeue_alternating():
    q = ArrayQueue()
    q.enqueue(1)
    q.dequeue()
    q.enqueue(2)
    assert q.dequeue() == 2

def test_large_number_elements():
    q = ArrayQueue()
    for i in range(1000):
        q.enqueue(i)
    for i in range(1000):
        assert q.dequeue() == i

def test_non_integer_inputs():
    q = ArrayQueue()
    q.enqueue("hello")
    q.enqueue([1, 2, 3])
    assert q.dequeue() == "hello"
    assert q.dequeue() == [1, 2, 3]

def test_boundary_resize():
    q = ArrayQueue()
    for i in range(20):  # Assuming initial size is 10 and resize happens at 2x
        q.enqueue(i)
    assert len(q._data) > 10

def test_randomized():
    import random
    q = ArrayQueue()
    elements = random.sample(range(100), 10)  # Generate 10 unique random elements
    for e in elements:
        q.enqueue(e)
    for e in elements:
        assert q.dequeue() == e

def test_state_after_exception():
    q = ArrayQueue()
    q.enqueue(1)
    with pytest.raises(Empty):
        q.dequeue()
        q.dequeue()  # This should raise an exception
    assert len(q) == 0