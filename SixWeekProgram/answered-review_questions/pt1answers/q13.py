
input1 = input("Input a string: ")
input2 = input("Input another string: ")

charlist = list(input1)
charlist2 = list(input2)

matches = []
for i in charlist:
    if i in charlist2 and i not in matches:
        matches.append(i)

print(matches)
