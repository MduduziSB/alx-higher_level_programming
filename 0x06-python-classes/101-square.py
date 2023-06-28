#!/usr/bin/python3
"""Creating Encapsulated Class Square"""


class Square:
    """definition of Inititiolization method"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """position getter method"""
    @property
    def position(self):
        return (self.__position)

    """position setter method"""
    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    """method used to compute area"""
    def area(self):
        return (self.__size * self.__size)

    """Prints a square"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for k in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")

    """Defines print() method"""
    def __str__(self):
        if self.__size == 0:
            return ""
        else:
            for k in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        return ""
