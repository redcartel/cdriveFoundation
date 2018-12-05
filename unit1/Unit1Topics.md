## Foundations Week 1 Day 1

#### Introduction, Expressions, Data Types

* There are two baisic ways of interacting with python, through python files and through the interactive environment.

* The python program will run through each line of a python file, executing each statement in order.

* The interactive environment will allow you to enter one line of code at a time and it will display the result (also known as a 'return value' for functions) of any expression that produces a result.

* Some of the basic *immutable* data types are integers, floats, booleans (True and False), strings, and the None value.

```
-7                      # an integer
89.5                    # a float (floating point number)
"hello"                 # a string
'Byte'                  # also a string
True                    # a boolean
None                    # the None type
```

* The literal form of a data type, like in the examples above, is one type of *expression*. Expressions are units of python code that evaluate to a value and can be combined in many ways.

* A literal of a data type evaluates to itself.

* Types of expressions include

    * Literal expressions of values, as above.

    * Variables on their own, which evaluate to their values

    * Function calls ```math.sqrt(5)```, ```max(3,4,5)```, or ```ord('A')```. The evaluated value of a function is called its *return value*. We say that ```ord('Z')``` *returns* 90.

    * Expressions combined with expressions using *operators*.

```
7 + 5

107 // 10

107 % 10

(3.14 ** 2) * 10

max(10, 100, 1000) + max(7, 49, 343)

("Byte " + "Academy ") * 3
```

    * Functions with expressions as arguments.

```

```

* To use functions that are part of *modules* like math, you must first import the 

* Most function call expressions ( like max(10, 20, 80) ) produce a value. Many functions that produce 'side effects' like, print, always have the value None.
