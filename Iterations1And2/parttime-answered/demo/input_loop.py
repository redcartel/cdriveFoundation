
prompt = "Input a number to sum, or 'done' to quit. "

num = input(prompt)
the_sum = 0

while num != "done":
    number = float(num)
    the_sum = the_sum + number
    num = input("Input a number to sum: ")

print("The sum is {}.".format(prompt))