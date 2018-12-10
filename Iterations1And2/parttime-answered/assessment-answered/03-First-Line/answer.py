filename = input("Input a filename: ")

wordlist = []
with open(filename, "r") as f:
    for line in f:
        firstword = line.strip().split()[0]
        wordlist.append(firstword)

n = 0
for word in wordlist[::-1]:
    n = n + 1
    print(n, ": ", word)