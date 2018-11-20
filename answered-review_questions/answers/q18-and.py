
def stringlist(mylist):
    newlist = []
    for i in mylist:
        newlist.append(str(i))
    return newlist


def printrange(myint):
    numlist = list(range(myint))
    x = stringlist(numlist)
    outputstring = ", ".join(x)
    outputstring = outputstring + ",and {}".format(myint)
    print(outputstring)

printrange(20)
