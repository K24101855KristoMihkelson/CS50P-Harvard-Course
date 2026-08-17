from loops.twttr import shorten


def test_shorten_vowels():
    assert shorten("Twitter") == "Twttr"
