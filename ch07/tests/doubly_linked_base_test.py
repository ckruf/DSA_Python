"""
Tests for the DoublyLinkedBase class.
"""
import pytest
from ch07.my_practice_implementations.doubly_linked_list import _DoublyLinkedBase, _Node


class TestInit:
    """
    Test the __init__ method of the DoublyLinkedBase class.
    """

    @staticmethod
    def test_init():
        test_base = _DoublyLinkedBase()
        assert test_base._size == 0
        assert isinstance(test_base._header, _Node)
        assert isinstance(test_base._trailer, _Node)
        assert test_base._header._next == test_base._trailer
        assert test_base._trailer._prev == test_base._header