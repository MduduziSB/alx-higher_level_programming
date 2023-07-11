#!/usr/bin/python3
"""module that implements inheritence"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Computes area"""
        return self.__width * self.__height

    def __str__(self):
        """returns a string reprresantation of area"""
        str_1 = "[" + "Rectangle" + "]"
        return "{} {}/{}".format(str_1, self.__width, self.__height)
