#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    less = number % 10
else:
    number *= -1
    less = number % 10
    number *= -1
    less *= -1
if less < 6 and less != 0:
    print(f"Last digit of {number} is {less} and is less than 6 and not 0")
elif less == 0:
    print(f"Last digit of {number} is {less} and is 0")
else:
    print(f"Last digit of {number} is {less} and is greater than 5")
