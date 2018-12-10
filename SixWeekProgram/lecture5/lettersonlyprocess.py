# demo.py

def alphaonly(word):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newword = ""
    for letter in word:
        if letter in alphabet:
            newword = newword + letter
    return newword

fileobject = open("tyger.txt", "r")
for line in fileobject:
    wordlist = line.split()
    newlist = []
    for word in wordlist:
        newlist.append(alphaonly(word))
    print(newlist)


