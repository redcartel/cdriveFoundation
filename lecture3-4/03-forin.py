"""
a new kind of loop: for... in

for element in sequence:
    ...

This kind of loop takes a sequence type and sets a variable equal to each
value in the sequence one at a time in order. the indented code block executes
once for each value the variable takes.

for element in range(5):
    print(element)

will produce:
0
1
2
3
4

for word in ("Call", "me", "Ishmael"):
    print(word)

will produce:
Call
me
Ishmael

Strings themselves are sequences of individual letters and characters:

for letter in "longfellow":
    print(letter + ":", end="")
print()

will produce
l:o:n:g:f:e:l:l:o:w:
"""

accumulator = ""
for number in range(0, 7):
    accumulator = accumulator + str(number)

assert accumulator == "0123456"

tracksum = 0
for value in (4000, 300, 20, 1):
    tracksum = tracksum + value

assert tracksum == 4321

"""
for i in range(10):
    print(i)

will produce the same results as

i = 0
while i < 10:
    print(i)
    i = i + 1

The for in range method of doing that kind of loop is the better way to do it
the code is simpler and there are fewer opportunities for simple errors.
"""

value = 0
sum1 = 0
while value < 10:
    sum1 = sum1 + value
    value = value + 1

sum2 = 0
for value in range(10):
    sum2 = sum2 + value

assert sum1 == sum2


"""
A common pattern is to put an if statement inside of a for statement to only
act on some of the values.

for i in range(20):
    if i > 15:
        print(i)

will produce
16
17
18
19
"""

vowels = "aeiouAEIOU"
accumulator = ""
for letter in "Old forum websites used to 'disemvowel' bad comments.":
    if letter not in vowels:
        accumulator = accumulator + letter

assert accumulator == "ld frm wbsts sd t 'dsmvwl' bd cmmnts."

"""
To create 'grids' of values or to execute actions over a range for every
value in a different range, you can put a for loop inside a for loop.

for number in range(3):
    print(number)
    for letter in "ABC":
        print("    {}".format(letter))

will print out:
0
    A
    B
    C
1
    A
    B
    C
2
    A
    B
    C

The outside loop works 'slowly' and the inside loop works 'quickly' running
through itself a full time for every element of the outside loop.

If an outside loop takes n steps and an inside loop takes m steps, the
double-indented code of the inside loop will execute n * m times.
"""

accumulator = ""
for letter in "ABC":
    for numbercharacter in "123":
        accumulator = accumulator + letter + numbercharacter + ","
    accumulator = accumulator + " "

assert accumulator == "A1,A2,A3, B1,B2,B3, C1,C2,C3, "
