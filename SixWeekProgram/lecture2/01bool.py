
# Booleans are the result operations and functions that test if something is true or not.

# equality
print("1 == 1: ", 1 == 1)
print("1 == 2: ", 1 == 2)

# non-equality
print("3 != 4: ", 3 != 4)
print("14 % 5 != 0: ", 14 % 5 != 0) # % can be used to test if a number is evenly divisible by another

# less than and greater than
print("10.5 < 10.55: ", 10.5 < 10.55)
print("10.5 > 10.55: ", 10.55 > 10.55)

# less than or equal to, greater than or equal to
print("5 <= 5: ", 5 <= 5)
print("100.00 >= 99: ", 100.00 >= 99)

# substring (is a string a part of another string?)
print('"abc" in "abcdefg": ', "abc" in "abcdefg")
print('"Python" in "Byte Academy Foundations": ', "Python" in "Byte Academy Foundations")

# use boolean operations to make multipart conditional tests

# not returns the opposite of a boolean value
print("not True: ", not True)
print('not "soda" in "coffee and tea"', not "soda" in "coffee and tea")

# and returns True if both the left and right are True
print("True and False: ", True and False)
print("5 < 10 and 1 < 5: ", 5 < 10 and 1 < 5)

# or returns True if either the left or right are True
print("True or False: ", True or False)
print('"A" in "ABC" or "A" in "abc"', "A" in "ABC" or "A" in "abc")

# some values will evaluate to True or False when they are evaluated as bools.
# most values are 'Truthy' zero or empty values are 'Falsy'
print("bool(0): ", bool(0))
print("bool(-1): ", bool(-1))
print("bool(100): ", bool(100))
print("bool(0.0): ", bool(0.0))
print('bool(""): ', bool(""))
print('bool("False"): ', bool("False"))
print('bool("0"): ', bool("0"))
