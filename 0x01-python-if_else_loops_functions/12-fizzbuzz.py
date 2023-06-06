#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        rem3 = i % 3
        rem5 = i % 5
        if rem3 == 0 and rem5 != 0:
            print("Fizz", end=" ")
        elif rem3 != 0 and rem5 == 0:
            print("Buzz", end=" ")
        elif rem3 == 0 and rem5 == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{}" .format(i), end=" ")
