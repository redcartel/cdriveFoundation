## Lists of lists

* copy the following code into a file and run it:

```python
rows = []
for rowindex in range(0,70,10):
    row = []
    for columnindex in range(0,10):
        row.append(rowindex + columnindex)
    rows.append(row)

print("Length of rows: {}".format(len(rows)))
print("rows[2]: {}".format(rows[2]))
print("rows[2][4], fifth column of third row:".format(rows[2][4]))
print()

for row in rows:
    for element in row:
        print("{:<3}".format(element), end="")
    print()
```

* really try to understand it.

* now, write code that prints a 2-dimensional subsection of the array of numbers just print the 4th through 8th columns of the 3rd through 5th rows.

```
 23 24 25 26 27
 33 34 35 36 37
 43 44 45 46 47
```