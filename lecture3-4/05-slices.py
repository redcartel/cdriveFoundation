"""
You can use indexing brackets [ ] to select sub-sequences of sequence types

The format is

sequence[start:stop]

or

sequence[start:stop:step]

Note the use of : colons instead of , commas to separate the values. Comma
separated index values are not used in the standard Python features, but are
used in some mathematics packages like Numpy and Pandas, which are common
tools for data science.

These values work much like the parameters for ranges. The sequence will begin
at the start value and step by 1 (or the step parameter) until the value before
the stop parameter.
"""

assert (1,2,3,4,5,6,7,8,9)[3:5] == (4,5)
assert "Byte Academy"[0:10:2] == "Bt cd"

"""
This creates a new sequence, even for a sequence that can be changed in-place
like a list
"""

a = ["a", "b", "c", "d", "e"]
b = a[2:5]
assert b == ["c", "d", "e"]
assert a == ["a", "b", "c", "d", "e"]

"""
You can use a negative step like with lists to go down from a start value to
a lower end value. It still contains the start value and does not contain the
end value.
"""

a = "0123456789"
assert a[8:1:-2] == "8642"

"""
You can ommit values to use defaults. Ommitting the start value default it to
0 (the first element). Ommitting the stop value defaults it to the step element
defaults it to 1
"""

assert [0,1,2,3,4,5,6,7,8,9,10][:5] == [0,1,2,3,4]
assert [0,1,2,3,4,5,6,7,8,9,10][7:] == [7,8,9,10]
assert [0,1,2,3,4,5][::-1] == [5,4,3,2,1,0]

"""
Using the default value for start and stop can be used to make a copy of a
list
"""

a = [1,2,3,4,5]
b = a[:]
assert b == [1,2,3,4,5]
