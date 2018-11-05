
def capsornot(word):
    if len(word) >= 4:
        return word.upper()
    else:
        return word

def processwordlist(wlist):
    result = []
    for i in range(len(wlist)):
        newword = capsornot(wlist[i])
        result.append(newword)
    return result

def processphrase(phrase):
    wlist = phrase.split()
    newlist = processwordlist(wlist)
    newphrase = " ".join(newlist)
    return newphrase

print(processphrase("an example list to test"))
