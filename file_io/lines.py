import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
    sys.exit("Usage: python lines.py file.py")

try:
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        lines = [line for line in file if line.strip() and not line.lstrip().startswith("#")]
    print(len(lines))
except FileNotFoundError:
    sys.exit("File does not exist")
