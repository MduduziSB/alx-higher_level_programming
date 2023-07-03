#!/usr/bin/python3
"""creation of class Rectangle"""


class Rectangle:
    """This is a Rectangle class"""
    def __init__(self, width=0, height=0):
        """This method initializes private class attributes"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width getter method"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Width setter method"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Height getter method"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """Height setter method"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
