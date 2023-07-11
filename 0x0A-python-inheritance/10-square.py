#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""module that implements Square class that inherits from Rectangle"""


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size