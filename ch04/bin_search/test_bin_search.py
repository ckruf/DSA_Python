from .bin_search import bin_search


def test_bin_search_empty_sequence():
    assert bin_search([], "a") is False


def test_bin_search_length_one():
    assert bin_search([5,], 5) == 0


def test_bin_search_even_length_success():
    sequence = [2, 3, 7, 10, 15, 84, 127, 489]
    assert bin_search(sequence, 3) == 1


def test_bin_search_even_length_fail():
    sequence = [2, 3, 7, 10, 15, 84, 127, 489]
    assert bin_search(sequence, 126) is False


def test_bin_search_even_edge_success():
    sequence = [2, 3, 7, 10, 15, 84, 127, 489]
    assert bin_search(sequence, 489) == len(sequence) - 1


def test_bin_search_odd_length_success():
    sequence = [2, 3, 7, 10, 15, 84, 127]
    assert bin_search(sequence, 3) == 1


def test_bin_search_odd_length_fail():
    sequence = [2, 3, 7, 10, 15, 84, 127]
    assert bin_search(sequence, 126) is False


def test_bin_search_odd_edge_success():
    sequence = [2, 3, 7, 10, 15, 84, 127]
    assert bin_search(sequence, 127) == len(sequence) - 1

