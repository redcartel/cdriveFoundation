
# problem 1

a = [0, 1, 4, 9, 16, 25, 36, 49]

print(len(a))
print(a[1])
a.append(64)  # this returns None!
print(a)

# problem 2

string = input("give me a string: ")
print("The last character of your string is {}".format(string[-1]))

# problem 3

print("The quick brown fox jumps over the lazy dog."[::3])

# problem 4

for letter in "Quiz time":
    if letter != " ":
        print("{}!".format(letter))
    else:
        print(letter)

# problem 5

for i in range(-10,50,7):
    print(i)
