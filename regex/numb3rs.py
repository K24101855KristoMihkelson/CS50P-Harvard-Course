import re


def validate(ip):
    if not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip):
        return False
    return all(0 <= int(part) <= 255 for part in ip.split("."))


print(validate(input("IPv4 Address: ")))
