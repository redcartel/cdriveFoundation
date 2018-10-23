# Expression Challenge

print ('Hi Carter, Danny mentioned you worked this week.')
hours = input ('How many hours did you work this week? ')
print ('Great!  Thanks for helping out!')
rate = input ('Can you remind me how many dollars you charge per hour? ')
hours = float(hours)
rate = float(rate)
total = hours * rate
total = float(total)
print ('Okay, I hope I am doing my math right.', 'Your total should be ${:.2f}' .format(total))
print ('{:.2f} hours at ${:.2f} per hour is ${:.2f}.' .format(hours, rate, total))


