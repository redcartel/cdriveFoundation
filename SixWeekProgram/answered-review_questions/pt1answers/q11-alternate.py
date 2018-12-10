
stringlist = []
while True:
    string = input("Input a string: ")
    if string == "done":
        break
    else:
        stringlist.append(string)

for i in range(len(stringlist)):
    stringlist[i] = stringlist[i].upper()

print(stringlist)
