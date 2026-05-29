import requests
import sys
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
try:
    x = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    c = requests.get("rest.coincap.io/v3/assets/bitcoin?apiKey=3bd95c6da89693101e211ec5588368768f604776e794b7754da4e52c33a771f6")
    d = c.json()
except requests.RequestException:
    sys.exit()
price = float(d["data"]["priceUsd"])
t = float(price * x)
print(f"${t:,.4f}")