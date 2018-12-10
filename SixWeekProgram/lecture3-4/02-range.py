"""
A new sequence type: range.

A range is a special type of object that represents a sequence of numbers.

range(10) will represent 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

if a varuable called stop is an integer greater than 0, range(stop) will be all
the values of n where 0 <= n < stop.

ranges always end one step before their stop value.

you can use [ ] indexing, len,  and the 'in' test just like you can with and 
tuples.
"""

assert range(10)[3] == 3
assert range(10)[0] == 0
assert range(10)[-1] == 9

assert len(range(10)) == 10

assert 7 in range(10)
assert 0 in range(10)
assert -1 not in range(10)
assert 10 not in range(10)

maximum = 7
myrange = range(maximum)

assert len(myrange) == 7
assert myrange[-1] == 6
assert 5 in myrange

"""
You can convert ranges into tuples to get the full list of the numbers they
represent. You won't need to do this in real code very often.
"""

assert tuple(range(5)) == (0, 1, 2, 3, 4)

"""
If you create a range with two parameters, you give a start and a stop value.

range(3,7) will represent 3, 4, 5, 6

If start and stop are integer variables, range(start, stop) will represent
all values of n where start <= n < stop
"""

assert tuple(range(5, 15)) == (5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
assert 0 not in range(5, 15)
assert range(5, 15)[-1] == 14

assert tuple(range(-2,2)) == (-2, -1, 0, 1)

start = 101
stop = 107
myrange = range(start, stop)
assert tuple(myrange) == (101, 102, 103, 104, 105, 106)

"""
If you create a range with three parameters, you add a step factor. That kind
of range starts at the start value and then steps up by the step until the last
value before the stop.

For instance, range(0,10,3) represents 0, 3, 6, 9
and range(5, 13, 2) represents 5, 7, 9, 11

if start, stop and step are integers, range(start, stop, step) will represents
all of the values of n where

n < stop and
n = start + 0 or n = start + (i * step) some positive integer i

range(5, 13, 2) is 5 + 0, 5 + 2, 5 + 4, 5 + 6, but 5 + 8 is not less than 13
sot that's the end.
"""

assert len(range(0, 14, 2)) == 7
assert range(0, 14, 2)[3] == 6
assert tuple(range(0, 14, 2)) == (0, 2, 4, 6, 8, 10, 12)

start = 0
stop = 100
step = 10
assert tuple(range(start, stop, step)) == (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)

"""
Lastly, you can have a negative step to count backwards. For this kind of range
the stop value will be less than the start value. The range still does include
the start value and does not include the stop value, even though that now
means that it is the lower value that is not included.

range(10, 0, -1) represents 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
"""

assert range(5, -2, -1)[0] == 5
assert len(range(5, -2, -1)) == 7
assert tuple(range(5, -2, -1)) == (5, 4, 3, 2, 1, 0, -1)

assert range(1000, 0, -1)[-1] == 1

start = 50
stop = 10
step = -5
assert tuple(range(start, stop, step)) == (50, 45, 40, 35, 30, 25, 20, 15)

"""
Under the hood:

Ranges do not generate all of the values they represent when they are created.
They store the pattern of the numbers, which takes up very little memory or
processor time.

This expression:
range(0, 999999999999999)[-1]

Would need more memory and time than would be possible if it had to actually
generate all of the numbers to find the last value. Instead python calculates
the result almost instantaneously.

Programmers used to other languages' way of doing for loops encounter python
ranges and feel like it is wasteful in terms of memory, but they are actually
very lean and mean.
"""
