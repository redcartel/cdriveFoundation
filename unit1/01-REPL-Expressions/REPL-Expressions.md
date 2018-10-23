## REPL & Expressions

#### Calculator

* There is nothing to turn in for this exercise.

* Start the python REPL by selecting run > python shell in IDLE. Verify that it is running a version of python equal to or greater than 3.5.

* REPL stands for Read-Evaluate-Print-Loop and that's what the python interpreter in interactive mode does. It reads python commands you type in, evaluates (interprets) them, prints the result, and then starts over again.

* Try using the interpreter as a calculator

* Add with +, multiply with ``*``, divide with /, and subtract with -

* Try storing the results of your calculations to variables. If you type in just the name of a variable, the interpreter will output its value. It is an error to check the value of a variable that hasn't been assigned one.

* Type 7 * 12 press enter, and then print the special variable _ (the underscore). What do you think _ does? (This only works in the REPL, don't use it in real programs).

* What happens when you do calculations with integers (like 0, 1, 2, 3) and floats (like 1.7, 8.1234, 3.14) together? What if the float is a whole number like 3.0?

* try this:

```
a = 0
a = a+1
```

* then press the up key to repeat a=a+1. Do it again. Do it a few times. Then print a.

* now enter a + 1. print a. press the up key and then hit enter to enter it again. print a.

* run the following commands:

```
a = 10
b = a
a = 5
print(b)
```

* do you understand what happened?

* The = sign by itself is the assignment operator. It is used to store a value in a variable. You will learn about testing for equality later, that uses a double ==. They are two different things!

* type 5 == 5

* type "7" == 7

* We'll come back to that!

* Try the ** (exponent) and // (floor division) and % (remainder or 'modulus') operators. Do you have a sense of what they do? 

* What does int(7.8) do?

* What does float(5) do?

## Strings

* Type ```a = "Learning to code is fun!" ```

* Type b = input("What is your name? ")

* What happens, what value does b have?

* Try using the print statement with different arguments. Try more than one argument separated by commas. ``` print("a", "b", 3, 7) ```

* type "I have ${}.".format(3.3333)

* type "I have ${:.2f}.".format(3.3333)

## The help() function

* Type in help(print) what do you see?

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

* Can you use the other functions without preceding them with math. ? Do you think you have an idea of what ``` import x ``` and ``` from x import y``` do?
