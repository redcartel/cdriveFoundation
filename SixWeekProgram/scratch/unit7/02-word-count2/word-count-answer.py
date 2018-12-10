import pprint

def cleanword(word):
    result = ""
    for letter in word.lower():
        if letter.isalpha() or letter == "'":
            result = result + letter
    return result

def getcounts(filename):
# read a file, return a dictionary whose keys are the
# words of the text and whose values are the number of
# times a word appears
    result = {}
    file_object = open(filename, "r")
    for line in file_object:
        for word in line.split():
            word = cleanword(word)
            if word in result:
                result[word] = result[word] + 1
            else:
                result[word] = 1
    return result


def buildlist(counts):
    result = []
    for key in counts:
        tup = (counts[key], key)
        result.append(tup)
    result.sort()
    result.reverse()
    return result


wordcounts = getcounts("mobydick.txt")
countlist = buildlist(wordcounts)
for element in countlist[0:20]:
    print("{} : {}".format(element[1], element[0]))
