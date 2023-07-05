#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """prints a square with the character #"""
    if (type(size) == float and size < 0) or type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
