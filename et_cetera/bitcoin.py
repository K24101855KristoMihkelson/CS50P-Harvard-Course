import sys

import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", timeout=10)
response.raise_for_status()
rate = response.json()["bpi"]["USD"]["rate_float"]

print(f"${amount * rate:,.4f}")
