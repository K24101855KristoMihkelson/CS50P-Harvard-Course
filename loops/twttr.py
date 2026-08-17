def shorten(word):
    return "".join(char for char in word if char.lower() not in {"a", "e", "i", "o", "u"})


if __name__ == "__main__":
    print(shorten(input("Input: ")))
