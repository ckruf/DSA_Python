from ch07.exercises.card_shuffle_43 import (
    PositionalList,
    card_shuffle
)


def test_shuffle_even():
    """
    Test the card_shuffle method with an even number of elements.
    """
    test_list = PositionalList()
    elems = ["A", "B", "C", "D", "E", "F"]
    for e in elems:
        test_list.add_last(e)
    assert [e for e in test_list] == elems
    card_shuffle(test_list)
    correct_order = ["A", "D", "B", "E", "C", "F"]
    assert [e for e in test_list] == correct_order
    

def test_shuffle_odd():
    """
    Test the card_shuffle method with an odd number of elements.
    """
    test_list = PositionalList()
    elems = ["A", "B", "C", "D", "E"]
    for e in elems:
        test_list.add_last(e)
    assert [e for e in test_list] == elems
    card_shuffle(test_list)
    correct_order = ["A", "D", "B", "E", "C"]
    assert [e for e in test_list] == correct_order


def test_shuffle_empty():
    """
    Test the card_shuffle method with an empty list.
    """
    test_list = PositionalList()
    card_shuffle(test_list)


def test_shuffle_single_element():
    """
    Test the card_shuffle method with a single-element list.
    """
    test_list = PositionalList()
    test_list.add_last("A")
    assert [e for e in test_list] == ["A",]
    card_shuffle(test_list)
    assert [e for e in test_list] == ["A",]