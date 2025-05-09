#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last digit == abs(number % 10)
if last digit > 5:
    print(f"Last digit of {number] is {last digit} and greater than 5")
elif last digit == 0:
    print(f"Last digit of {number} is {last digit} and 0")
else:
    print(f"last digit of {number] is {last digit} and less than 6 and not 0")
