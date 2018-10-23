#- This is a classic interview question for entry-level coding jobs.

#Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

#- So the beginning of the output will look like


# Decently ok with how this program works. Only problem is the range function is awkward with (1, 101).
# Prefer the for loop to while loop.
# Clever to put the fizzbuzz first.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)





