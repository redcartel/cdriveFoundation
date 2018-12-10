
timestring = input("How many hours did you work? ")
ratestring = input("At what hourly rate of pay? ")

time = float(timestring)
rate = float(ratestring)

check = time * rate

print("{} hours at ${:.2f} per hour is ${:.2f}.".format(time, rate, check))
