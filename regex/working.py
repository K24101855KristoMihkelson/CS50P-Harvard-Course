import re


def convert(s):
    match = re.fullmatch(r"(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)", s)
    if not match:
        raise ValueError

    h1, m1, ap1, h2, m2, ap2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if ap1 == "PM" and h1 != 12:
        h1 += 12
    if ap1 == "AM" and h1 == 12:
        h1 = 0
    if ap2 == "PM" and h2 != 12:
        h2 += 12
    if ap2 == "AM" and h2 == 12:
        h2 = 0

    return f"{h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}"


print(convert(input("Hours: ")))
