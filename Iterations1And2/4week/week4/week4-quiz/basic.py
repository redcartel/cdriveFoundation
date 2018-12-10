import requests

URL="https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt"

moby = requests.get(URL).text
lines = moby.split("\n")

count = 0
for line in lines:
    if "WHALE" in line.upper():
        count += 1
print(count)
