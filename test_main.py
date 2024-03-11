from main import generate_sequence


def test_generate_sequence():
    assert generate_sequence(10) == [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    assert generate_sequence(20) == [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]
    assert generate_sequence(0) == []
