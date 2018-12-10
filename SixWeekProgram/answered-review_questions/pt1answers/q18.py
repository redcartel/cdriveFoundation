
def stringlist(mylist):
    newlist = []
    for i in mylist:
        newlist.append(str(i))
    return newlist


def printrange(myint):
    numlist = list(range(myint+1))
    x = stringlist(numlist)
    outputstring = ", ".join(x)
    print(outputstring)

printrange(20)
