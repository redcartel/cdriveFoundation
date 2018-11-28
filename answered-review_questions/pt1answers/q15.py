
def isvowel(string):
    for i in string:
        if i not in "aeiouAEIOU":
            return False
    return True

def removevowel(string):
    newstring = ""
    for i in string:
        if isvowel(i):
            continue
        else:
            newstring = newstring + i
    return newstring

print(removevowel("Carter Adams"))
