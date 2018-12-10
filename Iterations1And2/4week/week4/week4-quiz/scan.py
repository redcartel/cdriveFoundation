import requests
import re


URL="https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt"

lines = requests.get(URL).text.split("\n")

count = 0
d = {}
for line in lines:
    m = re.search("(whale[^/:,.!?) ]*)", line.strip().lower())
    if m:
        words = m.groups()
        for word in words:
            word = word.lower()
            val = d.get(word, 0)
            d[word] = val + 1
for word in sorted(d, key=lambda w: (d[w], w)):
    print("{:<20}:{:>4}".format(word, d[word]))
