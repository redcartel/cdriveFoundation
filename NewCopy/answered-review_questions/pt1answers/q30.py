import pprint

testdict1 = {
        "a" : 5,
        "b" : 7,
        "c" : 9,
        "d" : 10
        }

testdict2 = {
        "b" : 100,
        "c" : 200,
        "e" : 400,
        "f" : 500
        }

testdict3 = {
        "f" : 1000,
        "c" : 2000,
        "z" : 3000
        }

def mergesums(dict1, dict2):
    newdict = {}
    for key in dict1:
        if key in dict2:
            newdict[key] = dict1[key] + dict2[key]
        else:
            newdict[key] = dict1[key]
    for key in dict2:
        if key not in newdict:
            newdict[key] = dict2[key]
    return newdict

def mergedicts(dictlist):
    newdict = {}
    for dictelement in dictlist:
        for key in dictelement:
            newdict[key] = newdict.get(key, 0) + dictelement[key]
    return newdict
            

pprint.pprint(mergesums(testdict1, testdict2))

pprint.pprint(mergedicts([testdict1, testdict2, testdict3]))
