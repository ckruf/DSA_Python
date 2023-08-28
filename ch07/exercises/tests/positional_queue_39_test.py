"""
File containing tests for exercise 7.39

Since all the methods are really just calling PositionalList methods, it does
not really make sense to test them individually, so only a test for 
general behavior is included.
"""
import pytest
from ch07.exercises.positional_queue_39 import PositionalQueue


def test_positional_queue():
    test_q = PositionalQueue()
    elements = [3, 6, 90, 87, 42, 12, 23, 40]
    # test enqueue
    for e in elements:
        test_q.enqueue(e)
    # test __len__
    assert len(test_q) == len(elements)
    # test __iter__
    assert [e for e in elements] == [e for e in test_q]
    # test first() and last()
    first_pos = test_q.first()
    last_pos = test_q.last()
    assert first_pos.element() == elements[0]
    assert last_pos.element() == elements[-1]
    # test after
    second_pos = test_q.after(first_pos)
    assert second_pos.element() == elements[1]
    # test before
    assert test_q.before(second_pos) == first_pos
    # test delete
    test_q.delete(second_pos)
    elements.remove(6)
    assert len(test_q) == len(elements)
    # test dequeue
    for e in elements:
        assert test_q.dequeue() == e
    assert len(test_q) == 0
    # test is_empty
    assert test_q.is_empty() is True
    # test first and last raise Exception when empty
    with pytest.raises(Exception):
        test_q.first()
    with pytest.raises(Exception):
        test_q.last()