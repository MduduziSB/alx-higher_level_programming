#!/usr/bin/python3
"""addition of two numbers module"""


def add_integer(a, b=98):
    """"
    Function that returns the sum of two numbers a and b.
    It works with numbers only:
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return (a + b)
