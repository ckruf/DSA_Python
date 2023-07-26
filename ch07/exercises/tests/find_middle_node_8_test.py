"""This file contains tests for exercise 7.8"""
import pytest
from ch07.exercises.find_middle_node_8 import find_middle_node
from ch07.my_practice_implementations.positional_list import PositionalList


def test_find_middle_node_empty_list():
    test_list = PositionalList()
    with pytest.raises(Exception):
        find_middle_node(test_list)


def test_find_middle_node_single_element_list():
    test_list = PositionalList()
    test_list.add_last("A")
    middle_node = find_middle_node(test_list)
    assert middle_node == test_list._header._next


def test_find_middle_node_odd_list():
    test_list = PositionalList()
    for e in "A", "B", "C":
        test_list.add_last(e)
    middle_node = find_middle_node(test_list)
    assert middle_node == test_list._header._next._next
    assert middle_node._element == "B"
    for e in "D", "E":
        test_list.add_last(e)
    middle_node = find_middle_node(test_list)
    assert middle_node == test_list._header._next._next._next
    assert middle_node._element == "C"


def test_find_middle_node_even_list():
    test_list = PositionalList()
    for e in "A", "B":
        test_list.add_last(e)
    middle_node = find_middle_node(test_list)
    assert middle_node == test_list._header._next
    assert middle_node._element == "A"

    for e in "C", "D":
        test_list.add_last(e)
    middle_node = find_middle_node(test_list)
    assert middle_node == test_list._header._next._next
    assert middle_node._element == "B"
