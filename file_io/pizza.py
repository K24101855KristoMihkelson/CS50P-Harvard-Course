import csv
import sys
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Usage: python pizza.py menu.csv")

try:
    with open(sys.argv[1], newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
