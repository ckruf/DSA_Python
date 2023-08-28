from ch07.exercises.favorites_list_mtf_purge_40 import FavoritesListMTFPurge, Position


def test_add_unique_elements():
    test_list = FavoritesListMTFPurge(3)
    for e in "A", "B", "C":
        test_list.access(e)
    
    assert len(test_list) == 3
    C_pos = test_list._data.first()
    assert isinstance(C_pos, Position)
    assert C_pos.element()._value == "C"
    assert C_pos.element()._access_cnt == 1
    B_pos = test_list._data.after(C_pos)
    assert isinstance(B_pos, Position)
    assert B_pos.element()._value == "B"
    assert B_pos.element()._access_cnt == 1
    A_pos = test_list._data.after(B_pos)
    assert isinstance(A_pos, Position)
    assert A_pos.element()._value == "A"
    assert A_pos.element()._access_cnt == 1

    test_list.access("D")
    assert len(test_list) == 3
    D_pos = test_list._data.first()
    assert isinstance(D_pos, Position)
    assert D_pos.element()._value == "D"
    assert test_list._data.after(D_pos) == C_pos
    assert test_list._data.after(C_pos) == B_pos == test_list._data.last()
    assert test_list._data.after(B_pos) is None


def test_repeating_elements():
    test_list = FavoritesListMTFPurge(3)
    for e in "A", "B", "C":
        test_list.access(e)

    assert len(test_list) == 3
    C_pos = test_list._data.first()
    assert isinstance(C_pos, Position)
    assert C_pos.element()._value == "C"
    assert C_pos.element()._access_cnt == 1
    B_pos = test_list._data.after(C_pos)
    assert isinstance(B_pos, Position)
    assert B_pos.element()._value == "B"
    assert B_pos.element()._access_cnt == 1
    A_pos = test_list._data.after(B_pos)
    assert isinstance(A_pos, Position)
    assert A_pos.element()._value == "A"
    assert A_pos.element()._access_cnt == 1

    test_list.access("A")  # all 3 should remain, A should move to front
    assert len(test_list) == 3
    assert test_list._data.first() == A_pos
    assert A_pos.element()._access_cnt == 2

    test_list.access("A")  # B should get purged now
    assert len(test_list) == 2
    assert A_pos.element()._access_cnt == 3
    # 2nd and last item should be C now
    assert test_list._data.after(A_pos) == C_pos == test_list._data.last()

    test_list.access("A")  # C should get purged now
    assert len(test_list) == 1
    assert A_pos.element()._access_cnt == 4
    assert test_list._data.first() == test_list._data.last() == A_pos
    