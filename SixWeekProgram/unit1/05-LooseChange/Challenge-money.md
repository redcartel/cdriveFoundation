## Loose Change 
---

##### Challenge

* Input an amount of money as a floating point number

* Print the number of American coins and bills needed to represent that float. (Round to the nearest penny)

* Hint: convert to an integer representing the number of cents in the value before you go forward. It's much easier to work with integers than with floating point numbers!

Use the following as denominations for your currencies:

```
    Penny: 1 cent
    Nickel: 5 cent
    Dime: 10 cent
    Quarter: 25 cent
    One-dollar bill
    Five-dollar bill
    Ten-dollar bill
    Twenty-dollar bill
    Fifty-dollar bill
    Hundred-dollar bill
```

#####Example input/output
```
[input]
12.33

[output]
0 $100
0 $50
0 $20
1 $10
0 $5
2 $1
1 quarters
3 dimes
0 nickel
3 pennies
```

* You can do this without if statements! Remember the // and % operators. Hint: Convert the amount input into cents as the first step. It's always easier to work with whole numbers than with floating point values.

* Extra extra challenge: Use proper plurals for bills when there are multiples or zero.

```
...
1 $10
0 $5s
2 $1s
1 quarter
3 dimes
0 nickels
3 pennies
```

hint:

```python
endings = ("s", "", "s", "s", "s")
# ending[1] = ?
```
