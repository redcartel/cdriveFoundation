letterlist = list("The quick brown fox jumps over the lazy dog")
print(letterlist[0])
print(letterlist[-1])
print(letterlist[3:7]) # start : stop works like ranges
print(letterlist[0:10:2])
print(letterlist[:10]) # omit values assumes 0 for start
print(letterlist[::2]) # or last element for end
print(letterlist[::-1]) # reverse a list

astring = "Slices work on strings too!"
print(astring[5:15])
print(astring[::-1])
