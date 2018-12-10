
def answerfunc(word):
    if len(word) <= 3:
        return word
    else:
        return word.upper()

def capswords(astring):
    result = ""
    for substring in astring.split():
        result = result + answerfunc(substring) + " "
    return result

processedstring = capswords("Mr. Carter Adams")
print(processedstring)
print(capswords("now is the time for all good men to come to the aid of their country"))