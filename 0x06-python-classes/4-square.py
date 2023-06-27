#!/usr/bin/python3
"""Creating Encapsulated Class Square"""


class Square:
    """definition of Inititiolization method"""
    def __init__(self, size=0):
        self.size = size

    """getter method"""
    @property
    def size(self):
        return (self.__size)

    """setter method"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """method used to compute area"""
    def area(self):
        return (self.__size * self.__size)
