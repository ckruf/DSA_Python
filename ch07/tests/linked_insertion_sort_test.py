from ch07.my_practice_implementations.positional_list import PositionalList

def insertion_sort(seq: PositionalList):
    if len(seq) < 2:
        return
    
    marker = seq.first()
    while marker != seq.last():
        to_be_inserted = seq.after(marker)
        walk = marker
        while to_be_inserted.element() < walk.element():
            walk = seq.before(walk)
        seq.add_before(walk, to_be_inserted.element())
        seq.delete(to_be_inserted)
        marker = seq.after(marker)


class TestLinkedInsertionSort:
    """
    Tests for insertion sort algorithm done on doubly linked list implemented
    as the PositionalList class/API.
    """

    @staticmethod
    def test_two_element_list():
        test_list = PositionalList()
        test_list.add_last(2)
        test_list.add_last(1)
        assert [2, 1] == [i for i in test_list]
        insertion_sort(test_list)
        assert [1, 2] == [i for i in test_list]