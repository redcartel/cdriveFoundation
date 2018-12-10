
def getdigits(number):
    newlist = []
    for i in str(number):
        newlist.append(int(i))
    return newlist

print(getdigits(2018))
