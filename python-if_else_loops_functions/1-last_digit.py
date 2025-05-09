#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
last_m = last - 10
if number >= 0:
    if 0 < last < 6:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
    elif last > 5:
        print(f"Last digit of {number} is {last} and is greater than 5")
    else:
        print(f"Last digit of {number} is 0 and is 0")
elif:
    if last != 0:
        print(f"Last digit of {number} is {last_m} and is less than 6 and not 0")
