#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = (-1 * number) % 10
print(f"Last digit of {number:d} is", end=" ")
if number > 0:
    if last and last <= 5:
        print(f"{last:d} and is less than 6 and not 0")
    if number % 10 and number % 10 > 5:
        print(f"{last:d} and is greater than 5")
    if number % 10 == 0:
        print(f"{last:d} and is 0")
else:
    if number % 10:
        print(f"-{last:d} and is less than 6 and not 0")
    else:
        print(f"{last:d} and is 0")
