phrase = input("Input a sentence: ")
excep = input("Input words not to capitalize: ")

words = excep.lower().split()

output = ""
for word in phrase.split():
    if word.lower() not in words:
        output = output + word.title() + " "
    else:
        output = output + word + " "

print(output)