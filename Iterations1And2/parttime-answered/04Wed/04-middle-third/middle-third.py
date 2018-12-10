inputstring = input("Give me a string and I'll tell you the middle third. ")

endpoint = len(inputstring)
start = endpoint // 3
end = (endpoint * 2) // 3

print()
print(len(inputstring))
print(inputstring[start:end])