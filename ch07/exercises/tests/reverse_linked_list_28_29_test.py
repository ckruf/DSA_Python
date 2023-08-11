"""This file contains tests for exercises 7.28 and 7.29"""
import pytest
from ch07.exercises.reverse_linked_list_28_29 import (
    LinkedList,
    reverse_list_recursively,
    reverse_list_iteratively,
)


@pytest.fixture(params=[reverse_list_recursively, reverse_list_iteratively])
def reversing_function(request):
    return request.param


@pytest.mark.parametrize(
    "elems",
    [
        [],
        [
            "A",
        ],
        ["A", "B", "C"],
    ],
)
def test_reverse_list(reversing_function, elems):
    test_list = LinkedList()
    for e in elems:
        test_list.add_last(e)
    assert [e for e in test_list] == elems
    reversing_function(test_list)
    assert [e for e in test_list] == list(reversed(elems))
