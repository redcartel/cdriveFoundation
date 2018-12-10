
def prompt_hours():
    hours = float(input("Give me your hours: "))
    return hours

def prompt_rate():
    rate = float(input("Give me the rate: "))
    return rate

def compute(hours, rate):
    if hours <= 40.0:
        total = hours * rate
    else:
        total = 40.0 * rate + (hours - 40.0) * (rate * 1.5)
    return total

# hoursworked = prompt_hours()
# payrate = prompt_rate()
# print(compute(hoursworked, payrate))

print(compute(prompt_hours(), prompt_rate()))
