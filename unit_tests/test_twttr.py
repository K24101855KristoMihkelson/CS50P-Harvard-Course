from twttr import shorten


def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"


def test_shorten_mixed():
    assert shorten("TwItTeR") == "TwtTR"


def test_shorten_numbers_and_punctuation():
    assert shorten("CS50! 2026") == "CS50! 2026"
