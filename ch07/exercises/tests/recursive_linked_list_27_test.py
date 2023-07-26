"""File containing unit tests for exercise 7.27"""
import pytest
from ch07.exercises.recursive_linked_list_27 import RecursiveLinkedList


class TestIsEmpty:
    """
    Tests for the 'is_empty()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_is_empty_empty():
        test_list = RecursiveLinkedList()
        assert test_list.is_empty() is True

    @staticmethod
    def test_is_empty_non_empty():
        test_list = RecursiveLinkedList("A")
        assert test_list.is_empty() is False


class TestAddLast:
    """
    Tests for the 'add_last()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_add_last_empty():
        test_list = RecursiveLinkedList()
        assert test_list._element is None
        assert test_list._rest is None
        test_list.add_last("A")
        assert test_list._element == "A"
        assert test_list._rest is None

    @staticmethod
    def test_add_last_single_element():
        test_list = RecursiveLinkedList()
        assert test_list._element is None
        assert test_list._rest is None
        test_list.add_last("A")
        assert test_list._element == "A"
        assert test_list._rest is None
        test_list.add_last("B")
        assert test_list._element == "A"
        assert isinstance(test_list._rest, RecursiveLinkedList)
        assert test_list._rest._element == "B"
        assert test_list._rest._rest is None

    @staticmethod
    def test_add_last_many_elements():
        test_list = RecursiveLinkedList()
        assert test_list._element is None
        assert test_list._rest is None
        test_list.add_last("A")
        assert test_list._element == "A"
        assert test_list._rest is None
        test_list.add_last("B")
        assert test_list._element == "A"
        assert isinstance(test_list._rest, RecursiveLinkedList)
        assert test_list._rest._element == "B"
        assert test_list._rest._rest is None
        test_list.add_last("C")
        assert test_list._rest._element == "B"
        assert isinstance(test_list._rest._rest, RecursiveLinkedList)
        assert test_list._rest._rest._element == "C"
        assert test_list._rest._rest._rest is None


class TestAddFirst:
    """
    Tests for the 'add_first()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_add_first_empty():
        test_list = RecursiveLinkedList()
        assert test_list._element is None
        assert test_list._rest is None
        test_list.add_first("A")
        assert test_list._element == "A"
        assert test_list._rest is None

    @staticmethod
    def test_add_first_single_element():
        test_list = RecursiveLinkedList()
        test_list.add_first("A")
        test_list.add_first("B")
        assert test_list._element == "B"
        assert isinstance(test_list._rest, RecursiveLinkedList)
        assert test_list._rest._element == "A"
        assert test_list._rest._rest is None

    @staticmethod
    def test_add_first_many_elements():
        test_list = RecursiveLinkedList()
        test_list.add_first("A")
        test_list.add_first("B")
        test_list.add_first("C")
        assert test_list._element == "C"
        assert isinstance(test_list._rest, RecursiveLinkedList)
        assert test_list._rest._element == "B"
        assert isinstance(test_list._rest._rest, RecursiveLinkedList)
        assert test_list._rest._rest._element == "A"
        assert test_list._rest._rest._rest is None


class TestDeleteFirst:
    """
    Tests for the 'delete_first()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_delete_first_empty():
        test_list = RecursiveLinkedList()
        with pytest.raises(Exception):
            test_list.delete_first()

    @staticmethod
    def test_delete_first_single_element():
        test_list = RecursiveLinkedList()
        test_list.add_first("A")
        assert test_list._element == "A"
        assert test_list._rest is None
        test_list.delete_first()
        assert test_list._element is None
        assert test_list._rest is None

    @staticmethod
    def test_delete_first_multiple_elements():
        test_list = RecursiveLinkedList()
        test_list.add_first("A")
        test_list.add_first("B")
        assert test_list._element == "B"
        assert isinstance(test_list._rest, RecursiveLinkedList)
        assert test_list._rest._element == "A"
        assert test_list._rest._rest is None
        test_list.delete_first()
        assert test_list._element == "A"
        assert test_list._rest is None
        test_list.delete_first()
        assert test_list._element is None
        assert test_list._rest is None


class TestDeleteLast:
    """
    Tests for the 'delete_last()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_delete_last_empty():
        test_list = RecursiveLinkedList()
        with pytest.raises(Exception):
            test_list.delete_last()

    @staticmethod
    def test_delete_last_single_element():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        assert test_list._element == "A"
        assert test_list._rest is None
        test_list.delete_last()
        assert test_list._element is None
        assert test_list._rest is None

    @staticmethod
    def test_delete_last_multiple_elements():
        test_list = RecursiveLinkedList()
        for e in "A", "B", "C":
            test_list.add_last(e)
        assert test_list._element == "A"
        assert isinstance(test_list._rest, RecursiveLinkedList)
        assert test_list._rest._element == "B"
        assert isinstance(test_list._rest._rest, RecursiveLinkedList)
        assert test_list._rest._rest._element == "C"
        assert test_list._rest._rest._rest is None
        test_list.delete_last()
        assert test_list._rest._rest is None
        assert test_list._rest._element == "B"
        test_list.delete_last()
        assert test_list._rest is None
        assert test_list._element == "A"
        test_list.delete_last()
        assert test_list._element is None
        assert test_list._rest is None


class TestFirst:
    """
    Tests for the 'first()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_first_empty():
        test_list = RecursiveLinkedList()
        with pytest.raises(Exception):
            test_list.first()

    @staticmethod
    def test_first_non_empty():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        test_list.add_last("B")
        assert test_list.first() == "A"


class TestLast:
    """
    Tests for the 'last()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_last_empty():
        test_list = RecursiveLinkedList()
        with pytest.raises(Exception):
            test_list.last()

    @staticmethod
    def test_last_single_element():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        assert test_list.last() == "A"

    @staticmethod
    def test_last_multiple_elements():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        assert test_list.last() == "A"
        test_list.add_last("B")
        assert test_list.last() == "B"
        test_list.add_last("C")
        assert test_list.last() == "C"


class TestIsEmpty:
    """
    Tests for the 'is_empty()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_is_empty_empty():
        test_list = RecursiveLinkedList()
        assert test_list.is_empty() is True

    @staticmethod
    def test_is_empty_not_empty():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        assert test_list.is_empty() is False


class TestLen:
    """
    Tests for the '__len__()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_len_empty():
        test_list = RecursiveLinkedList()
        assert len(test_list) == 0

    @staticmethod
    def test_len_single_element():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        assert len(test_list) == 1

    @staticmethod
    def test_len_multiple_elements():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        test_list.add_last("B")
        assert len(test_list) == 2
        test_list.add_last("C")
        assert len(test_list) == 3


class TestIter:
    """
    Tests for the '__iter__()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_iter_empty():
        test_list = RecursiveLinkedList()
        for _ in test_list:
            assert False

    @staticmethod
    def test_iter_single_element():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        assert [
            "A",
        ] == [e for e in test_list]

    @staticmethod
    def test_iter_multiple_elements():
        test_list = RecursiveLinkedList()
        test_list.add_last("A")
        test_list.add_last("B")
        assert [
            "A",
            "B",
        ] == [e for e in test_list]
        test_list.add_last("C")
        assert ["A", "B", "C"] == [e for e in test_list]


class TestStr:
    """
    Test for the '__str__()' method of the RecursiveLinkedList class.
    """

    @staticmethod
    def test_str():
        test_list = RecursiveLinkedList()
        regular_list = []
        for e in "A", "B", "C":
            test_list.add_last(e)
            regular_list.append(e)
            assert str(test_list) == str(regular_list)


class TestGeneral:
    """
    Test of a series of operations on the RecursiveLinkedList class.
    """

    @staticmethod
    def test_general():
        test_list = RecursiveLinkedList()
        test_list.add_last("B")
        test_list.add_first("A")
        test_list.add_last("C")
        assert ["A", "B", "C"] == [e for e in test_list]
        assert len(test_list) == 3
        assert test_list.is_empty() is False
        assert test_list.last() == "C"
        test_list.delete_last()
        test_list.add_last("D")
        assert test_list.last() == "D"
        assert test_list.first() == "A"
        test_list.delete_first()
        test_list.delete_last()
        test_list.delete_first()
        test_list.add_first("Z")
        test_list.add_first("Y")
        test_list.add_first("X")
        assert ["X", "Y", "Z"] == [e for e in test_list]
