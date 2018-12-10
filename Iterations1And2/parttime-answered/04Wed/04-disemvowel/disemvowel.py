inputstring = input("Give me an input string to disemvowel: ")

output = []
vowels = 'aeiouyAEIOUY'

for letter in inputstring:
    if letter not in vowels:
        output.append(letter)

print("".join(output))