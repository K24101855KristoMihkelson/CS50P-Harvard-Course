import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python lines.py <filename>")

try:
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        count = sum(1 for line in file if line.strip() and not line.lstrip().startswith("#"))
    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
