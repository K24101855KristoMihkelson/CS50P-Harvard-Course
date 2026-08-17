from loops.plates import is_valid


def test_plate_starts_with_letters():
    assert is_valid("CS50")
    assert not is_valid("50CS")
