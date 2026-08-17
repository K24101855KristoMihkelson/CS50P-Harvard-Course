import re


def parse(s):
    match = re.search(r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9_-]+)"', s)
    if not match:
        return None
    return match.group(1).replace("/embed/", "/")


print(parse(input("HTML: ")))
