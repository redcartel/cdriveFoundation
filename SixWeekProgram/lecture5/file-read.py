
def method1():
    fileobject = open("tyger.txt", "r")
    for line in fileobject:
        print(line)
    fileobject.close()

def method2():
    with open("tyger.txt", "r") as fileobject:
        for line in fileobject:
            print(line)


method1()
