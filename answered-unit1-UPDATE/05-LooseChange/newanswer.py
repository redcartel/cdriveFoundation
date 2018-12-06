
amount = float(input("How much money do you have? "))

amount = round(amount * 100)

hundreds = amount // 10000
print("{} $100".format(hundreds))
amount = amount - hundreds * 10000

fifties = amount // 5000
print("{} $50".format(fifties))