
total = 0

def increase():
    global total
    total = total+1

def decrease():
    global total
    total = total-1

increase()
increase()
print(total)
decrease()
decrease()
decrease()
print(total)
