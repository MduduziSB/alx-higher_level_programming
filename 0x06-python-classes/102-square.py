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
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """method used to compute area"""
    def area(self):
        return (self.__size * self.__size)

    """method that defines == comparison to a square"""
    def __eq__(self, other):
        return (self.area() == other.area())

    """method that defines != comparison to a square"""
    def __ne__(self, other):
        return (self.area() != other.area())

    """method that defines < comparison to a square"""
    def __lt__(self, other):
        return (self.area() < other.area())

    """method that defines > comparison to a square"""
    def __gt__(self, other):
        return (self.area() > other.area())

    """method that defines >= comparison to a square"""
    def __ge__(self, other):
        return self.area() >= other.area()

    """method that defines >= comparison to a square"""
    def __le__(self, other):
        return self.area() <= other.area()
