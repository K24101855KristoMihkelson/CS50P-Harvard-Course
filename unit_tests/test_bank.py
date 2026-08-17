from conditionals.bank import greeting


def test_greeting_hello():
    assert greeting("hello") == 0


def test_greeting_h():
    assert greeting("hey") == 20


def test_greeting_other():
    assert greeting("good morning") == 100
