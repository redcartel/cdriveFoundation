## Day 5 Exercise 2 - Processing Files

#### Extracting data

Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

#### Hint

* Remember the 'in' test for if statements to find if a string is part of a bigger string, and remember split() to break a string into parts separated by blank space.

* Don't write it all at once. First just find the lines, then isolate the numbers, then do the math.
