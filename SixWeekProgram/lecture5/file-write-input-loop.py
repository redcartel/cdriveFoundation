
fileobject = open("output.txt", "w")

keeplooping = True

while keeplooping:
    string = input("input 'done' or a string to add to the file: ")
    if string == 'done':
        keeplooping = False
    else:
        print(string, file=fileobject)

fileobject.close()
