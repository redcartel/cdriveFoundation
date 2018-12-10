"""
Sequence types contain multiple values in an order. You can access their contents with indexing.

A string is a sequence of individual letters
"""

assert "Example"[1] == "x"

"""
Indexing starts counting at 0 and goes to the length-1. So a string with 8 characters will have values for thestring[0] to thestring[7]
"""

assert "abcdefgh"[0] == "a"
assert "abcdefgh"[7] == "h"
# "abcdefgh"[8] would raise an exception

"""
You index sequences stored in variables the same way.
"""

examplestring = "stored value"
assert examplestring[3] == "r"

"""
Negative indices count from the end. -1 is the last character.
"""

assert "abcdefgh"[-1] == "h"
assert "abcdefgh"[-3] == "f"

"""
Another simple type of sequence is the tuple. It is a group of values of any type, separated by commas in parentheses.
"""

tuppowers = (0,10,100,1000)
assert tuppowers[2] == 100
assert len(tuppowers) == 4

tupnames = ("Carter", "Kenso", "Greg")
assert tupnames[-1] == "Greg"
assert len(tupnames) == 3

"""
Sequence types support testing for containment. You can use 'in'
in a conditional to ask if a certain element is in a sequence.
"""

assert "x" in "xyz"
assert 8 in (1,2,4,8,16,32,64,128,356)
assert " " not in "alltogethernow"

answer = "yes"
istrue = False
if answer in ("yes", "no"):
    istrue = True
assert istrue

name = "Serge"
isfalse = False
if name in ("Eduardo", "Sam", "Peter"):
    isfalse = True

assert isfalse == False
