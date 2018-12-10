
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getword(string):
    word = ""
    for letter in string:
        if letter in alphabet:
            word = word + letter
    return word

def longestword(line):
    longestw = ""
    for wordchunk in line.split():
        word = getword(wordchunk)
        if len(word) > len(longestw):
            longestw = word
    return longestw

def findlongest(filename):
    longestw = ""
    file_object = open(filename, "r")
    for line in file_object:
        linelongest = longestword(line)
        if len(linelongest) > len(longestw):
            longestw = linelongest
    file_object.close()
    return longestw

print(findlongest("mobydick.txt"))
