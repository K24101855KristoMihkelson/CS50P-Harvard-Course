import re


def parse(s):
    if match := re.search(r"<iframe[^>]*src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)\"", s):
        return f"https://youtu.be/{match.group(1)}"
    return None


print(parse(input("HTML: ")))
