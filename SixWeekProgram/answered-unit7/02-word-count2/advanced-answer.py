
def splitline(line):
    wordlist = line.split()
    for i in range(len(wordlist)-1, -1, -1):
        # assigning a list to a slice replaces those elements with the elements of the right hand side
        # you can use split with characters other than space
        wordlist[i:i+1] = wordlist[i].split("-")
    return wordlist


def stripword(word):
    newword = ""
    for char in word:
        # .isalpha() tests if a string is a letter. we also check for apostrophes. there are other is... tests for strings.
        if char.isalpha() or char == "'":
            newword = newword + char
    return newword.lower()


def countwords(filename):
    counts = {}
    # this is the preferred way to open a file. the file_object is open only for the block introduced by with and it is closed automatically, even if there is an error
    with open(filename, "r") as file_object:
        for line in file_object:
            words = []
            for word in splitline(line):
                words.append(stripword(word))

            for word in words:
    # .get retrieves a default value, its second parameter, if the key does not exist, instead of throwing a KeyError.
                counts[word] = counts.get(word, 0) + 1
    return counts


def sorted_dict(counts):
    countlist = []
    # dictionary.items() creates tuples of key, value, so this pattern gives you access to the elements in the dictionary
    for word, count in counts.items():
        countlist.append((count, word))
    # a list of tuples will sort by the first element in each tuple, here the count of a word
    countlist.sort()
    return countlist

    # this is the preferred way to have code that executes when you type python filename.py. this allows you to also import the file as a module without code executing, which lets you use your functions in other files
if __name__ == "__main__":
    counts = countwords("mobydick.txt")
    countlist = sorted_dict(counts)
    print("top 20 words:")
    for tuple in countlist[len(countlist)-1:-21:-1]:
        print("{:<10} - {}".format(tuple[1], tuple[0]))
    print()
    print("and to satisfy my own curiosity:")
    print("{:<10} - {}".format("Ahab", counts["ahab"]))
    print("{:<10} - {}".format("Ishmael", counts["ishmael"]))
    print("{:<10} - {}".format("Moby", counts["moby"]))
    print("{:<10} - {}".format("Starbuck", counts["starbuck"]))
    print("{:<10} - {}".format("Pequod", counts["pequod"]))
    print("{:<10} - {}".format("Whale", counts["whale"]))
    print("{:<10} - {}".format("God", counts["god"]))
