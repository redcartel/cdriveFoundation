
def longerstring(string1, string2):
    a = len(string1)
    b = len(string2)
    if a > b:
        return string1 
    else:
        return string2

print(longerstring("Carter", "Adams"))
