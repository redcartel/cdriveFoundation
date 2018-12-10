
def arevowels(word):
    for letter in word:
        if letter not in "aeiouAEIOU":
            return False
    return True

print(arevowels("aei"))
print(arevowels("aaaaak"))
