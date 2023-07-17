"""This file contains tests for exercise 7.9"""
from ch07.my_practice_implementations.positional_list import PositionalList
from ch07.exercises.concatenate_doubly_linked_lists_9 import concatenate_doubly_linked


def test_concatenate_empty_lists():
    first = PositionalList()
    second = PositionalList()
    assert [] == [e for e in first] == [e for e in second]
    assert len(first) == 0
    assert len(second) == 0
    concatenate_doubly_linked(first, second)
    assert [] == [e for e in first]
    assert len(first) == 0

    assert [] == [e for e in second]
    assert len(second) == 0


def test_concatenate_full_to_empty():
    first = PositionalList()
    second = PositionalList()
    elems = ["A", "B", "C"]
    for e in elems:
        first.add_last(e)
    assert [] == [e for e in second]
    assert elems == [e for e in first]
    assert len(first) == 3
    assert len(second) == 0
    concatenate_doubly_linked(first, second)
    
    assert elems == [e for e in first]
    assert len(first) == 3
    
    assert [] == [e for e in second]
    assert len(second) == 0


def test_concatenate_empty_to_full():
    first = PositionalList()
    second = PositionalList()
    elems = ["A", "B", "C"]
    for e in elems:
        second.add_last(e)
    assert [] == [e for e in first]
    assert elems == [e for e in second]
    assert len(second) == 3
    assert len(first) == 0
    concatenate_doubly_linked(first, second)
    assert elems == [e for e in first]
    assert len(first) == 3

    assert [] == [e for e in second]
    assert len(second) == 0


def test_concatenate_two_full():
    first = PositionalList()
    second = PositionalList()
    first_elems = ["A", "B", "C",]
    second_elems = ["D", "E", "F"]
    all_elems = first_elems + second_elems
    for e in first_elems:
        first.add_last(e)
    for e in second_elems:
        second.add_last(e)
    assert first_elems == [e for e in first]
    assert second_elems == [e for e in second]
    assert len(first) == 3
    assert len(second) == 3
    concatenate_doubly_linked(first, second)
    assert [e for e in first] == all_elems
    assert len(first) == 6
    assert [] == [e for e in second]
    assert len(second) == 0
