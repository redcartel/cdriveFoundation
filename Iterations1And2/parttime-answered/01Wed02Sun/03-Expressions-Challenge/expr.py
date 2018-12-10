rate = input(" What is the rate per hour worked? ")
rate = float(rate)
hours = input(" How many hours were worked? ")
hours = float(hours)

print("Total pay is ${:0.2f}".format(rate * hours))