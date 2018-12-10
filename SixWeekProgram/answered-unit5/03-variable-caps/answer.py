def caplong(string):
    if len(string) >= 4:
        return string.upper()
    else:
        return string

def capstringlist(strlist):
    result = []
    for str in strlist:
        result.append(caplong(str))
    return result

def processphrase(phrase):
    wordlist = phrase.split()
    newlist = capstringlist(wordlist)
    return " ".join(newlist)

phrase = input("Give me a phrase: ")
print(processphrase(phrase))
