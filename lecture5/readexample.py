
fileobject = open("tyger.txt", "r")
for line in fileobject:
    print(line, end="")

fileobject.close()
