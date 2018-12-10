
counts = {}

myinput = ""
while myinput != "done":
    word = input("give me a word: ")
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1



myinput = ""
while myinput != "done":
    word = input("give me a word: ")
    counts[word] = counts.get(word, 0) + 1
