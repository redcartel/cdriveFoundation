"""
A sequence you can modify: lists

Lists are like tuples, but their contents can be changed.

You have seen strings joined into new strings with the + operator. You can do
the same with tuples.
"""

assert "abc" + "def" == "abcdef"
assert (1,2,3) + (10,20,30) == (1, 2, 3, 10, 20, 30)
a = (1, 2, 3)
a = a + (4, 5, 6)
assert a == (1, 2, 3, 4, 5, 6)

"""
But when you do this, you aren't changing the tuple or string on the left. you
are taking the two pieces and then making a whole new value that is copies
of them joined together.

Lists, which are expressed like tuples but with square brackets, are
different. Their contents can change without making a whole new copy.

if a = (1, 2, 3)
you can't say a[1] = 4 to change a, trying to do that raises an error.

but when you create a list and store it in a variable
b = [1, 2, 3]
you can modify its contents
"""

b = [1, 2, 3]
b[1] = 4
assert b == [1, 4, 3]

"""
Lists are collections like the strings, tuples, and ranges we have seen.

You can check len, index their sub elements, and loop through them with for
loops.
"""

alist = ["first", "second", "third", "fourth"]
assert len(alist) == 4
assert alist[1] == "second"

accumulator = ""
for string in alist:
    accumulator = accumulator + string

assert accumulator == "firstsecondthirdfourth"

"""
Lists can be mofified by several special methods
"""

alist = [1, 2, 3, 4]
alist.append(5)
assert alist == [1,2,3,4,5]

blist = ["a", "b", "c", "d", "e", "f"]
lastvalue = blist.pop()
assert lastvalue == "f"
assert blist == ["a", "b", "c", "d", "e"]

blist.remove("c")
assert blist == ["a", "b", "d", "e"]

del(blist[2])
assert blist == ["a", "b", "e"]

blist.insert(2, "Z")
assert blist == ["a", "b", "Z", "e"]

clist = [0, -5, -10, -15, 10, 20, -20, 15, 5]
clist.sort()
assert clist == [-20, -15, -10, -5, 0, 5, 10, 15, 20]

"""
There are several others covered in Automate the Boring Stuff
"""
