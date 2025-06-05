from a2w5p2 import calculate_fare


def test_calculate_fare():
    assert calculate_fare(2) == 7.75
    assert calculate_fare(1.4) == 6.50
