import csv
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py before.csv after.csv")

try:
    with open(sys.argv[1], newline="", encoding="utf-8") as before, open(sys.argv[2], "w", newline="", encoding="utf-8") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
