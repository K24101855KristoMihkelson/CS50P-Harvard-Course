import csv
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py before.csv after.csv")

students = []

try:
    with open(sys.argv[1], "r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            last, first = row["name"].split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(students)
