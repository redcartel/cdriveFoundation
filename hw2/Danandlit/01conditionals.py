#- Use input() to prompt the user to enter an integer and use int() to convert the string to an integer value. Store the result in a variable.
#- If the number is equal to zero, print "It is zero!" If it is not, print "It's not zero!"
#- Print "Less than 10!" when the number is less than 10. Print "Between 10 and 20" when the number is between 10 and 20 (including 10 and 20) and print "Big number!" if the number is greater than 20.
#- Print "Not a two digit number" if the number is a not two digit number."
#- If the number is even print "It is even!"
#- If the number is divisible by three, print "Divisible by three!"
#- If the number is divisible by four, print "Divisible by four!"
#- More than one of the above three tests can be true and print their message. If none of them are true, print "Not divisible by two, three, or four."
#- If the number is not divisible by seven, multiply it by seven. If it is divisible by seven, divide it by seven. Then print the result.
#- That's it!


num = int(input("Enter an integer: "))

if num == 0:
    print("It is zero!")
else:
    print("It is not zero!")

if num < 10:
    print("Less than 10!")
elif 10 <= num <= 20:
    print("Between 10 and 20")
elif num > 20:
    print("Big number!")

if not 10 <= num < 100:
    print("Not a two digit number")

if num % 2 == 0:
    print("It is even!")

if num % 3 == 0:
    print("Divisible by three!")

if num % 4 == 0:
    print("Divisible by four!")

if not (num % 2 == 0 or num % 3 == 0 or num % 4 == 0):
    print("Not divisible by two, three, or four.")

if not (num % 7 == 0):
    print(num * 7)
else:
    print(num // 7)
