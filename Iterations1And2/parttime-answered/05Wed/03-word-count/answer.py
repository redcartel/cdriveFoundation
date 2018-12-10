
word_counts = {}

def processline(line):
    for word in line.lower().split():
        word_counts[word] = 1 + word_counts.get(word, 0)

def sortfunc(element):
    return -1 * word_counts[element]

if __name__ == "__main__":
    with open("article.txt", "r") as file_object:
        for line in file_object:
            processline(line)
    for key in sorted(word_counts, key=sortfunc)[0:10]:
        print("{:<30}: {}".format(key, word_counts[key]))