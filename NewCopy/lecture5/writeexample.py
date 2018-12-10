
fileobject = open("newfile.txt", "w")
mystrings = ["first line", "second line", "third line", "fourth line"]
for string in mystrings:
    print(string, file=fileobject)

fileobject.close()
