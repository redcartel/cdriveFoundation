
phrase = input("Input a phrase: ")
length = len(phrase)
print("The length is {} characters.".format(length))

start = length // 3
stop = (length * 2) // 3
print(phrase[start:stop])
