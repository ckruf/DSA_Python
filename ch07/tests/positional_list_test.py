"""
Tests for the PositionalList class.
NOTE: These tests are dependent on a correct implementation of the
DoublyLinkedBase class.
"""
import pytest
from ch07.my_practice_implementations.positional_list import PositionalList


class TestFirst:
    """
    Tests for the 'first()' method of the PositionalLIst class.
    """

    @staticmethod
    def test_first_single_element():
        test_list = PositionalList()
        inserted_pos = test_list._insert_between(
            "A", test_list._header, test_list._trailer
        )
