"""This file contains tests for exercise 7.5"""
import pytest
from ch07.my_practice_implementations.positional_list import PositionalList
from ch07.exercises.find_max_11 import max


def test_max_empty():
    test_list = PositionalList()
    with pytest.raises(Exception):
        max(test_list)


def test_max_single_element():
    test_list = PositionalList()
    test_list.add_last(10)
    assert max(test_list) == 10


def test_max_multiple_elements():
    test_list = PositionalList()
    test_list.add_last(10)
    test_list.add_last(6)
    test_list.add_last(3)
    assert max(test_list) == 10
    test_list.add_first(15)
    assert max(test_list) == 15
    test_list.add_last(100)
    assert max(test_list) == 100