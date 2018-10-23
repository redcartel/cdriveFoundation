## The 'try' and 'except' statements

#### Bonus material

* Look at this code:

```
try:
    yearstring = input("Enter a year: ")
    year = int(yearstring)
except ValueError:
    print("That was not a valid number.")
```

* If code in a try block causes an error to occur, python will first look for an except block that handles that specific error.

* If that except block exists, that code is run instead of python giving an error message and quitting.

* This is often used for data the program can't be sure about, such as user input, reading files, or data from the internet.

#### Challenge:

* Write a program that asks the user to input integers until they are done. To be done, they input 'done.'

* Each time they enter an integer, it prints whether or not that number is even.

* If they enter a value that is not 'done' and is not a valid number, it gives a friendly error message and then asks them to try again.

* You'll need a while loop. You don't have to use it, but the 'continue' statement from the textbook might be useful.

#### Extra challenge

* Look over your previous exercises for places where the input() statement is used. Can any of these programs be improved with some basic exception handling?
