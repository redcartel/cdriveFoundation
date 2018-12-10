
# first function

def isnumdiv7(number):
    if number % 7 == 0:
        return True
    else:
        return False

# second function


def isstring10(string):
    if len(string) >= 10:
        return True
    else:
        return False

def firstletter(string):
    return string[0]

def zerolist(length):
    result = []
    for i in range(length):
        result.append(0)
    return result

def printlist(alist):
    # index = 1
    for i in range(len(alist)):
        print(str(i+1) + ". " + str(alist[i]))

# printlist(["a", "b", "c", "d"])

def segment(string):
    result = []
    for n in range(len(string) // 2):
        substr = string[2 * n:2 * (n+1)]
        result.append(substr)
    if len(string) % 2 == 1:
        result.append(string[-1])
    return result

print(segment("Carter Adams"))

# zerolist(4) => [0, 0, 0, 0]

