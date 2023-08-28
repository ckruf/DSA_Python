"""File containing tests for exercise 7.40"""
from ch07.exercises.favorites_list_mtf_purge_40 import FavoritesListMTFPurge


class TestGeneral:
    @staticmethod
    def test_access_sequence_unique_elements():
        """
        Test that FavoritesListMTFPurge behaves correctly when unique elements
        are added. 
        For example: 
        - set purge_limit to 3
        - access  "A", "B", "C", "D"
        Final state of the list should be:
        - "D", "C", "B" 
        - "A" should be purged (has not been accessed in last 3 accesses)
        - most recently accessed elements are moved to the front
        """
        test_list = FavoritesListMTFPurge(3)
        for e in "A", "B", "C":
            test_list.access(e)
        assert len(test_list) == 3
        first_pos = test_list._data.first()
        second_pos = test_list._data.after(first_pos)
        third_pos = test_list._data.after(second_pos)
        assert first_pos.element()._value == "C"
        assert second_pos.element()._value =="B"
        assert third_pos.element()._value == "A"
        assert third_pos == test_list._data.last()
        assert (first_pos.element()._count == second_pos.element()._count 
                == third_pos.element()._count == 1)

        test_list.access("D")
        assert len(test_list) == 3
        first_pos = test_list._data.first()
        second_pos = test_list._data.after(first_pos)
        third_pos = test_list._data.after(second_pos)
        assert first_pos.element()._value == "D"
        assert second_pos.element()._value =="C"
        assert third_pos.element()._value == "B"
        assert third_pos == test_list._data.last()

    @staticmethod
    def test_access_sequence_repeated():
        """
        Test that FavoritesListMTFPurge behaves correctly when we first add unique
        elements to the list, and then repeatedly access a single element.
        For example:
        - set purge limit to 3
        - access "A", "B", "C", "A", "A", "A"
        Final state of the list should be:
        - "A" only
        - "B" should be purged after penultimate "A" access
        - "C" should be purges after last "A" access
        """
        test_list = FavoritesListMTFPurge(3)
        for e in "A", "B", "C":
            test_list.access(e)
        assert len(test_list) == 3
        first_pos = test_list._data.first()
        second_pos = test_list._data.after(first_pos)
        third_pos = test_list._data.after(second_pos)
        assert first_pos.element()._value == "C"
        assert second_pos.element()._value =="B"
        assert third_pos.element()._value == "A"
        assert third_pos == test_list._data.last()
        assert (first_pos.element()._count == second_pos.element()._count 
                == third_pos.element()._count == 1)

        print("before first A access", test_list._data)
        test_list.access("A")
        print("after first A access", test_list._data)

        
        # should remove 'B'
        test_list.access("A")
        assert len(test_list) == 2
        assert test_list._data.last().element()._value == "C"

        # should remove 'C'
        test_list.access("A")
        assert len(test_list) == 1
        assert test_list._data.last().element()._value == "A"
        assert test_list._data.first().element()._count == 4
    