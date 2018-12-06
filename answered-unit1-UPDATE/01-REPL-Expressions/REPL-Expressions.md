## REPL & Expressions

#### Calculator

* There is nothing to turn in for this exercise.

* Start the python REPL by selecting run > python shell in IDLE. Verify that it is running a version of python equal to or greater than 3.5.

* REPL stands for Read-Evaluate-Print-Loop and that's what the python interpreter in interactive mode does. It reads python commands you type in, evaluates (interprets) them, prints the result, and then starts over again.

* Try using the interpreter as a calculator

* Add with +, multiply with ``*``, divide with /, and subtract with -

* What is 100 / 7?

* What is 100 * 7?

* What is 100.0 * 7?

* What is 100 // 7?

* What is 23 % 10?

* What is 6 + 7 * 8?

* What is (6 + 7) * 8?

* What is 5 ** 3?

* What is 10 + 10?

* What is 10 + 10.0?

* What is int(3.8)

* What is round(3.8)

* Store the value 10000 in a variable called principal. Store the value 1.05 in a variable called interest. Enter the line ``` principal = principal * interest ```. Using either print or by entering the variable name see what the value of principal is. Use the up key to repeat the multiplication a few times. Now see what the value is. 

* run the following commands:

```
a = 10
b = a
a = 5
print(b)
```

* Do you understand what happened? Assignment like this takes the value stored in a and stores it in b. It does not create a permanent equality.

* The = sign by itself is the assignment operator. It is used to store a value in a variable. You will learn about testing for equality later, that uses a double ==. They are two different things!

* type 5 == 5

* type "7" == 7

* We'll come back to that!

## Strings

* Type ```a = "Learning to code is fun!" ```

* Type b = input("What is your name? ")

* What happens, what value does b have?

* Try using the print statement with different arguments. Try more than one argument separated by commas. ``` print("a", "b", 3, 7) ```

* type ```"I have ${}.".format(3.3333)```

* type ```"I have ${:.2f}.".format(3.3333)```

* type ```"ho " * 3```

* type ```"Academy" in "Byte Academy"```

* type ```int("17")```

* type ```float("3.14159")```

* type ```int("number 8")```

* type ```"emphasize".upper()```

* type ```len("emphasize")```

## Some tuples

* type ```t = (1,2,3)```

* type ```t[0]```

* type ```t[2]```

* type ```s = ("Python", "programming", "is", "fun")```

* type ```"programming" in s```

* type ```len(s)```

## The help() function

* Type in help(print) what do you see?

* (use the 'q' key to get out of help view)

* You can use help on most python functions, and modules (we'll cover modules later).

* Note, if the help message prevents you from entering code after you open it, press 'q' to get out.

## Exiting

* The quit() command exits the REPL.

## Extra investigation, the math module

* Type ```import math```

* Type math.sqrt(16)

* Type help(math) to see what's available. The q key exits this view.

* Use the up and down arrows to navigate a long help article. Press 'q' to exit a help view.

* Type help(math.cosh)

* Spend some time exploring this. Try the different functions on different inputs. Notice that some of them need more than one number. We'll talk about functions soon.

* Type ```from math import sqrt```

* Now type sqrt(16)
