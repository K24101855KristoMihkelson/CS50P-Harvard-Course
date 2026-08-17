import csv
import sys

from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Usage: python pizza.py menu.csv")

try:
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        table = list(csv.reader(file))
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
