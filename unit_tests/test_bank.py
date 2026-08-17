from bank import value


def test_hello():
    assert value("hello") == 0


def test_h_prefix():
    assert value("hey") == 20


def test_other():
    assert value("good morning") == 100
