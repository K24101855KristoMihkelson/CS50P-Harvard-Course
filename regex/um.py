import re


def count(s):
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


print(count(input("Text: ")))
