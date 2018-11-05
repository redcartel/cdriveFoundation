somestrings = ["one", "two", "three", "four"]

def method1(stringlist):
    fileobject = open("outputfile.txt", "w")
    for string in stringlist:
        print(string, file=fileobject)
    fileobject.close()

def method2(stringlist):
    with open("outputfile.txt", "w") as fileobject:
        for string in stringlist:
            print(string, file=fileobject)
    fileobject.close()
