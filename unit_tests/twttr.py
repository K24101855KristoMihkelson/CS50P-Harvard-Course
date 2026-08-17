def shorten(word):
    return "".join(ch for ch in word if ch.lower() not in "aeiou")
