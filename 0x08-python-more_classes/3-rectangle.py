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

    def area(self):
        """Method to compute area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Method to compute perimeter of a rectangle"""
        if self.__width == 0 or self.height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """Represents a rectangle with hatches('#')"""
        rec = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i < self.__height - 1:
                rec.append('\n')
        return "".join(rec)
