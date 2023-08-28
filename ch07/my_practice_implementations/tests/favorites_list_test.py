"""
Tests for the FavoritesList class.
NOTE: these tests are dependent on a correct implementation of the 
PositionalList class!
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
from ch07.my_practice_implementations.favorites_list import (
    FavoritesList,
    Position,
    Item,
)


@pytest.fixture
def favorites_list_abcd_cnt_1():
    """
    Fixture to provide a 'FavoritesList' instance with 4 'Item' instances,
    whose _element are the letters 'A', 'B', 'C', 'D' and whose _access_count
    is 1 (not 0, because that's not a legitimate state, as items can only
    be added throught the 'access' method, which puts their count at 1).
    """
    favorites_list = FavoritesList()
    elements = ("A", "B", "C", "D")
    items = [Item(element, 1) for element in elements]
    for item in items:
        favorites_list._data.add_last(item)
    yield favorites_list


class TestFindInList:
    """
    Tests for the '_find_in_list() private method of the FavoritesList class.
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


class TestMoveUp:
    """
    Tests for the '_move_up()' private method of the FavoritesList class.
    """

    @staticmethod
    def test_move_up_no_move(favorites_list_abcd_cnt_1):
        """
        Test the '_move_up()' private method, when the element to be moved up should
        not move up at all. This test calls the method on all the elements in a list
        where access counts are equal, so the list should remain unchanged.
        """
        original_order = [item._element for item in favorites_list_abcd_cnt_1._data]
        walk = favorites_list_abcd_cnt_1._data.first()
        while walk is not None:
            favorites_list_abcd_cnt_1._move_up(walk)
            walk = favorites_list_abcd_cnt_1._data.after(walk)
        order_after_moving = [item._element for item in favorites_list_abcd_cnt_1._data]
        assert original_order == order_after_moving

    @staticmethod
    def test_move_up_one_position():
        """
        Test the '_move_up()' private method, when the element to be moved up should
        move by one position.
        """
        items = [Item("A", 5), Item("B", 4), Item("C", 2), Item("D", 3)]
        favorites_list = FavoritesList()
        for item in items:
            favorites_list._data.add_last(item)
        position_D = favorites_list._data.last()
        favorites_list._move_up(position_D)
        new_correct_order = ["A", "B", "D", "C"]
        new_actual_order = [item._element for item in favorites_list._data]
        assert new_correct_order == new_actual_order

    @staticmethod
    def test_move_up_multiple_positions():
        """
        Test the '_move_up()' private method, when the element to be moved up should
        move up multiple positions.
        """
        items = [
            Item("A", 5),
            Item("B", 4),
            Item("C", 2),
            Item("D", 2),
            Item("E", 3),
            Item("F", 2),
        ]
        favorites_list = FavoritesList()
        for item in items:
            favorites_list._data.add_last(item)
        position_F = favorites_list._data.last()
        position_E = favorites_list._data.before(position_F)
        assert position_E.element()._element == "E"
        favorites_list._move_up(position_E)
        new_correct_order = ["A", "B", "E", "C", "D", "F"]
        new_actual_order = [item._element for item in favorites_list._data]
        assert new_correct_order == new_actual_order

    @staticmethod
    def test_move_up_to_first():
        """
        Test the '_move_up()' private method, when the element to be moved up should
        move up to the top position.
        """
        items = [Item("A", 1), Item("B", 1), Item("C", 1), Item("D", 2)]
        favorites_list = FavoritesList()
        for item in items:
            favorites_list._data.add_last(item)
        position_D = favorites_list._data.last()
        assert position_D.element()._element == "D"
        favorites_list._move_up(position_D)
        new_correct_order = ["D", "A", "B", "C"]
        new_actual_order = [item._element for item in favorites_list._data]
        assert new_correct_order == new_actual_order


class TestAccess:
    """
    Tests for the 'access' method of the FavoritesList class.
    NOTE these tests depend on the correct implementation of the _find_in_list
    and _move_up private methods.
    """

    @staticmethod
    def test_access_existing(favorites_list_abcd_cnt_1):
        """
        Test the 'access' method when accessing an existing element.
        Should increase the element's access count and move the element up.
        """
        D_position = favorites_list_abcd_cnt_1._find_in_list("D")
        assert isinstance(D_position, Position)
        D_element = D_position.element()
        assert isinstance(D_element, Item)
        assert D_element._element == "D"
        original_count = D_element._access_count
        favorites_list_abcd_cnt_1.access("D")
        D_position = favorites_list_abcd_cnt_1._find_in_list("D")
        D_element = D_position.element()
        updated_count = D_element._access_count
        assert updated_count == original_count + 1
        # because all items had equal access counts, D should now be at the front
        assert favorites_list_abcd_cnt_1._data.first().element() == D_element

    @staticmethod
    def test_access_non_existing(favorites_list_abcd_cnt_1):
        """
        Test the 'access' method when accessing a non-existing element.
        This should create a new Item instance with the element and an access count
        of 1, and add it to the back of the list.
        """
        non_existent = favorites_list_abcd_cnt_1._find_in_list("E")
        assert non_existent is None
        favorites_list_abcd_cnt_1.access("E")
        position_E = favorites_list_abcd_cnt_1._data.last()
        item_E = position_E.element()
        assert isinstance(item_E, Item)
        assert item_E._element == "E"
        assert item_E._access_count == 1

    @staticmethod
    def test_access_initially_empty():
        """
        Test the 'access' method on an initially empty list.
        This test was written because my implementation of PositionalList
        raised ValueError when calling 'first()' on an empty list, which then
        caused 'access()' to fail when using on initially empty FavoritesList.
        """
        test_list = FavoritesList()
        assert len(test_list) == 0
        test_list.access("A")
        assert len(test_list) == 1
        assert test_list._data.first().element() == Item("A", 1)


class TestRemove:
    """
    Tests for the 'remove' method of the FavoritesList class.
    """

    def test_remove_existing(self, favorites_list_abcd_cnt_1):
        position_D = favorites_list_abcd_cnt_1._find_in_list("D")
        assert position_D is not None
        favorites_list_abcd_cnt_1.remove("D")
        position_D = favorites_list_abcd_cnt_1._find_in_list("D")
        assert position_D is None

    def test_remove_non_existing(self, favorites_list_abcd_cnt_1):
        position_E = favorites_list_abcd_cnt_1._find_in_list("E")
        assert position_E is None
        favorites_list_abcd_cnt_1.remove("E")
        position_E = favorites_list_abcd_cnt_1._find_in_list("E")
        assert position_E is None


class TestTop:
    """
    Tests for the 'top' method of the FavoritesList class.
    """

    @staticmethod
    def test_fails_on_zero(favorites_list_abcd_cnt_1):
        """
        Test that ValueError is raised when 0 is provided as argument.
        """
        with pytest.raises(ValueError) as e_info:
            for elem in favorites_list_abcd_cnt_1.top(0):
                pass

    @staticmethod
    def test_fails_on_greater_than_length(favorites_list_abcd_cnt_1):
        """
        Test that ValueError is raised when a number greater than the length
        of the list is provided.
        """
        with pytest.raises(ValueError) as e_info:
            for elem in favorites_list_abcd_cnt_1.top(
                len(favorites_list_abcd_cnt_1) + 1
            ):
                pass

    @staticmethod
    def test_succeeds_one():
        """
        Test that top() succeeds when 1 is provided as argument.
        """
        items = [
            Item("A", 5),
            Item("B", 4),
            Item("C", 2),
        ]
        favorites_list = FavoritesList()
        for item in items:
            favorites_list._data.add_last(item)
        assert [elem for elem in favorites_list.top(1)] == [
            "A",
        ]

    @staticmethod
    def test_succeeds_all(favorites_list_abcd_cnt_1):
        """
        Test that top() succeeds when the length of the list is provided as
        argument.
        """
        length = len(favorites_list_abcd_cnt_1)
        elems = [elem for elem in favorites_list_abcd_cnt_1.top(length)]
        assert elems == ["A", "B", "C", "D"]

    @staticmethod
    def test_succeeds_some(favorites_list_abcd_cnt_1):
        """
        Test that top() succeeds when the provided length is greater than 1 and
        less than the length of the list.s
        """
        assert [elem for elem in favorites_list_abcd_cnt_1.top(2)] == ["A", "B"]


class TestClear:
    """
    Test for the 'clear()' method of the FavoritesList class. Done for
    exercise 7.22
    """

    @staticmethod
    def test_clear(favorites_list_abcd_cnt_1):
        assert len(favorites_list_abcd_cnt_1) == 4
        favorites_list_abcd_cnt_1.clear()
        assert len(favorites_list_abcd_cnt_1) == 0


class TestResetCounts:
    """
    Test for the 'reset_counts()' method of the FavoritesList class. Done for
    exercise 7.23.
    """

    @staticmethod
    def test_reset_counts(favorites_list_abcd_cnt_1):
        original_order = []
        for item in favorites_list_abcd_cnt_1._data:
            original_order.append(item._element)
            assert item._access_count == 1
        favorites_list_abcd_cnt_1.reset_counts()
        new_order = []
        for item in favorites_list_abcd_cnt_1._data:
            new_order.append(item._element)
            assert item._access_count == 0
        assert original_order == new_order
