hours = float(input("How many hours did you work last week?"))
rate = float(input("How much is your rate per hour?"))


total = hours * rate

print("Total", total)
print("{:.2f} hours at ${:.2f} per hour is ${:.2f} total ".format(hours, rate, total))

##"35 hours at $11.50 per hour is $402.50."
