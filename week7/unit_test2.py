from unit_test import add


def test_add_pos_numbers():
    assert add(5, 6) == 11
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-5, -5) == -10
    assert add(-4, -1) == -5
