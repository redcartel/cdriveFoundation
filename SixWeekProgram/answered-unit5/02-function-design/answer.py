
def func1(number):
    if number % 7 == 0:
        return True
    else:
        return False

print("func1(6)", func1(6))
print("func1(14)", func1(14))
print()
def func2(string):
    if len(string) >= 10:
        return True
    else:
        return False

longstr = "Now is the time for all good folks to come to the aid of their country - Patrick Henry (sort of)"
shortstr = "Vote 11/6"
print("func2(longstr)", func2(longstr))
print("func2(shortstr)", func2(shortstr))
print()
def func3(length):
    newlist = []
    for i in range(0, length):
        newlist.append(0)
    return newlist

print("func3(5)", func3(5))

def func4(inputlist):
    for i in range(0, len(inputlist)):
        print("{}. {}".format(i+1, inputlist[i]))

print("func4(['first', 'things', 'first'])", func4(['first', 'things', 'first']))
print()
# they start to get hard here...

def func5(inputlist):
    answerlist = []
    iterations = len(inputlist) // 2

    for i in range(iterations):
        answerlist.append(inputlist[i*2:i*2+2])

    if len(inputlist) % 2 == 1:
        answerlist.append(inputlist[-1])

    return answerlist

print("func5('carter adams')", func5('carter adams'))
print("func5('kenso trabing')", func5('kenso trabing'))
print()

def func6(number):
    output = "+"
    for i in range(number):
        output = output + "-"
    output = output + "+"
    print(output)

print("func6(8):")
func6(8)
print()

def func7(width, height):
    rows = []
    for count in range(height):
        row = []
        for count2 in range(width):
            row.append(None)
        rows.append(row)
    return rows

import pprint
print("pprint.pprint is a useful function for printing out big data structures")
print("pprint.pprint(func7(6,3)):")
pprint.pprint(func7(6,3))
