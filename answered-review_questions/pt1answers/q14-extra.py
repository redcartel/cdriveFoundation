
def isvowel(string):
    for i in string:
        if i not in "aeiouAEIOU":
            return False
    return True

print(isvowel("aaab"))
