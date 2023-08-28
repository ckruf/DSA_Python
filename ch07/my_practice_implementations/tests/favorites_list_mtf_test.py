"""
Tests for the FavoritesListMTF class.
NOTE: these tests are dependent on a correct implementation of the
PositionalList class! Tests for this class are in a separate file.
"""
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.absolute()
dsa_python_dir = src_dir.parent.absolute()
sys.path.insert(0, str(dsa_python_dir))

import pytest
from ch07.my_practice_implementations.favorites_list_mtf import (
    FavoritesListMTF,
    PositionalList,
    Position,
    Item,
)


@pytest.fixture
def favorites_list_abcd_cnt_1():
    """
    Fixture to provide a 'FavoritesListMTF' instance with 4 'Item' instances,
    whose _element are the letters 'A', 'B', 'C', 'D' and whose _access_count
    is 1 (not 0, because that's not a legitimate state, as items can only
    be added throught the 'access' method, which puts their count at 1).
    """
    favorites_list = FavoritesListMTF()
    elements = ("A", "B", "C", "D")
    items = [Item(element, 1) for element in elements]
    for item in items:
        favorites_list._data.add_last(item)
    yield favorites_list


class TestFindInList:
    """
    Tests for the '_find_in_list()' private method of the FavoritesListMTF
    class.
    """

    @staticmethod
    def test_find_in_list_first(favorites_list_abcd_cnt_1):
        """
        Test the '_find_in_list()' private method, when the element we are trying
        to find is in the first position of the list.
        """
        position_A = favorites_list_abcd_cnt_1._find_in_list("A")
        assert isinstance(position_A, Position)
        item_A = position_A.element()
        assert isinstance(item_A, Item)
        assert item_A._element == "A"

    @staticmethod
    def test_find_in_list_middle(favorites_list_abcd_cnt_1):
        """
        Test the '_find_in_list()' private method, when the element we are trying
        to find is in a middle position of the list.
        """
        position_C = favorites_list_abcd_cnt_1._find_in_list("C")
        assert isinstance(position_C, Position)
        item_C = position_C.element()
        assert isinstance(item_C, Item)
        assert item_C._element == "C"

    @staticmethod
    def test_find_in_list_last(favorites_list_abcd_cnt_1):
        """
        Test the '_find_in_list()' private method, when the element we are trying
        to find is in the last position of the list.
        """
        position_D = favorites_list_abcd_cnt_1._find_in_list("D")
        assert isinstance(position_D, Position)
        item_D = position_D.element()
        assert isinstance(item_D, Item)
        assert item_D._element == "D"

    @staticmethod
    def test_find_in_list_non_existent(favorites_list_abcd_cnt_1):
        """
        Test the '_find_in_list()' private method, when the element we are trying
        to find is not found in the list.
        In this case, the method should return None.
        """
        position_E = favorites_list_abcd_cnt_1._find_in_list("E")
        assert position_E is None


class TestInit:
    """
    Tests for the __init__ method of the FavoriteListMTF class.
    """

    @staticmethod
    def test_init():
        """
        Test that the '__init__()' method initializes a FavoritesListMTF
        instance with the _data attribute being an instance of PositionalList.
        """
        test_list = FavoritesListMTF()
        assert isinstance(test_list._data, PositionalList)


class TestLen:
    """Tests for the '__len__()' method of the FavoritesListMTF class."""

    @staticmethod
    def test_len_when_zero():
        test_list = FavoritesListMTF()
        assert len(test_list) == 0

    @staticmethod
    def test_len_when_non_zero():
        test_list = FavoritesListMTF()
        test_list._data.add_first("A")
        assert len(test_list) == 1


class TestIsEmpty:
    """Tests for the 'is_empty()' method of the FavoritesListMTF class"""

    @staticmethod
    def test_is_empty_when_empty():
        test_list = FavoritesListMTF()
        assert test_list.is_empty() is True

    @staticmethod
    def test_is_empty_when_not_empty():
        test_list = FavoritesListMTF()
        test_list._data.add_last("A")
        assert test_list.is_empty() is False


class TestAccess:
    """Tests for the 'access()' method of the FavoritesListMTF class."""

    @staticmethod
    def test_access_non_existent(favorites_list_abcd_cnt_1):
        """
        Test 'access()' method when accessing an element which is previously
        not present in the list. This should:
        - create the Item, put it into a list, and give it an access_count of 1
        - put the Item at the front of the list
        """
        print("test_access_non_existent", favorites_list_abcd_cnt_1)
        # assert item not previously in list
        assert favorites_list_abcd_cnt_1._find_in_list("E") is None
        favorites_list_abcd_cnt_1.access("E")
        # assert element has been added
        assert favorites_list_abcd_cnt_1._find_in_list("E") is not None
        # assert it's been placed to the front of the list
        newly_added = favorites_list_abcd_cnt_1._data.first().element()
        assert isinstance(newly_added, Item)
        assert newly_added._element == "E"
        # assert access count has been set to 1
        assert newly_added._access_count == 1

    @staticmethod
    def test_access_existent_not_first(favorites_list_abcd_cnt_1):
        """
        Test the 'access()' method when accessing an element which is
        already present in the list (but not in first position). This should:
        - increase the Item's access_count
        - insert the item at the front of the list
        - remove the item from its original position
        """
        # assert item is in list to begin with
        C_pos = favorites_list_abcd_cnt_1._find_in_list("C")
        assert isinstance(C_pos, Position)
        elems = [item._element for item in favorites_list_abcd_cnt_1._data]
        assert elems.count("C") == 1
        # assert initial access count
        assert C_pos.element()._access_count == 1
        pos_list = favorites_list_abcd_cnt_1._data
        # assert C is in third position before accessing
        assert pos_list.after(pos_list.after(pos_list.first())) == C_pos

        favorites_list_abcd_cnt_1.access("C")
        # assert item has been moved to fron
        C_pos = favorites_list_abcd_cnt_1._data.first()
        assert isinstance(C_pos, Position)
        C_item = C_pos.element()
        assert isinstance(C_item, Item)
        assert C_item._element == "C"
        # assert access count has increased
        assert C_item._access_count == 2
        # make sure that C has been removed from original position
        elems = [item._element for item in favorites_list_abcd_cnt_1._data]
        assert elems.count("C") == 1


class TestRemove:
    """Tests for the 'remove()' method of the FavoritesListMTF class."""

    @staticmethod
    def test_remove_existent(favorites_list_abcd_cnt_1):
        """
        Test that the 'remove()' method removes an existing element
        from the list.
        """
        elems = [item._element for item in favorites_list_abcd_cnt_1._data]
        assert elems == ["A", "B", "C", "D"]
        favorites_list_abcd_cnt_1.remove("C")
        elems = [item._element for item in favorites_list_abcd_cnt_1._data]
        assert elems == ["A", "B", "D"]

    @staticmethod
    def test_remove_non_existent(favorites_list_abcd_cnt_1):
        """
        Test that the 'remove()' method doesn't do anything (and does not fail)
        when removing an element which is not in the list.
        """
        elems = [item._element for item in favorites_list_abcd_cnt_1._data]
        assert elems == ["A", "B", "C", "D"]
        favorites_list_abcd_cnt_1.remove("E")
        elems = [item._element for item in favorites_list_abcd_cnt_1._data]
        assert elems == ["A", "B", "C", "D"]


class TestTop:
    """Tests for the 'top()' method of the FavoritesListMTF class."""

    @staticmethod
    def test_top_some():
        """
        Test that the 'top()' method works correctly when some items (but not
        all) are selected. The list is ordered in access_cnt order.
        """
        test_list = FavoritesListMTF()
        items = [Item("A", 1), Item("B", 2), Item("C", 3), Item("D", 4), Item("E", 5)]
        for item in items:
            test_list._data.add_last(item)
        top_three_elements = [elem for elem in test_list.top(3)]
        assert top_three_elements == ["E", "D", "C"]

    @staticmethod
    def test_top_some_random_order():
        """
        Test that the 'top()' method works correctly when some items (but not
        all) are selected. The list is random order.
        """
        test_list = FavoritesListMTF()
        items = [
            Item("B", 2),
            Item("E", 5),
            Item("C", 3),
            Item("D", 4),
            Item("A", 1),
        ]
        for item in items:
            test_list._data.add_last(item)
        top_three_elements = [elem for elem in test_list.top(3)]
        assert top_three_elements == ["E", "D", "C"]

    @staticmethod
    def test_top_all():
        """
        Test that the 'top()' method works correctly when all items
        are selected.
        """
        test_list = FavoritesListMTF()
        items = [
            Item("B", 2),
            Item("E", 5),
            Item("C", 3),
            Item("D", 4),
            Item("A", 1),
        ]
        for item in items:
            test_list._data.add_last(item)
        top_three_elements = [elem for elem in test_list.top(5)]
        assert top_three_elements == ["E", "D", "C", "B", "A"]

    @staticmethod
    def test_top_one():
        """
        Test that the 'top()' method works when one item is selected
        """
        test_list = FavoritesListMTF()
        items = [
            Item("B", 2),
            Item("E", 5),
            Item("C", 3),
            Item("D", 4),
            Item("A", 1),
        ]
        for item in items:
            test_list._data.add_last(item)
        top_three_elements = [elem for elem in test_list.top(1)]
        assert top_three_elements == [
            "E",
        ]

    @staticmethod
    def test_raises_exception_on_zero():
        """
        Test that the 'top()' method raises an Exception when it is given
        0 as argument.
        """
        test_list = FavoritesListMTF()
        with pytest.raises(Exception):
            for elem in test_list.top(0):
                pass

    @staticmethod
    def test_raises_exception_on_greater_than_length(favorites_list_abcd_cnt_1):
        """
        Test that the 'top()' method raises an Exception when it is given
        a number greater than the length of the list as an argument.
        """
        assert len(favorites_list_abcd_cnt_1) < 5
        with pytest.raises(Exception):
            for elem in favorites_list_abcd_cnt_1.top(5):
                pass


class TestGeneral:
    """General test of a sequence of operations on FavoritesListMTF"""

    @staticmethod
    def test_general():
        test_list = FavoritesListMTF()
        assert len(test_list) == 0
        elems = ["A", "B", "C", "D", "E"]
        for elem in elems:
            test_list.access(elem)
        assert len(test_list) == len(elems)
        assert test_list._data.first().element() == Item("E", 1)
        test_list.access("C")
        assert test_list._data.first().element() == Item("C", 2)
        test_list.access("C")
        test_list.access("B")
        assert test_list._data.first().element() == Item("B", 2)
        assert [elem for elem in test_list.top(2)] == ["C", "B"]
        test_list.access("E")
        test_list.remove("C")
        assert len(test_list) == len(elems) - 1
        assert [elem for elem in test_list.top(2)] == ["E", "B"]
