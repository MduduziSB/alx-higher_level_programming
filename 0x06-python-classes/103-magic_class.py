#!/usr/bin/python3
import math
"""define MagicClass"""


class MagicClass:
    """Defining attributes and methods"""
    def __init__(self, radius=0):
        """Initialisation of class attribute"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Method to compute area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Metod used to compute circumfurance"""
        return (2 * math.pi * self.__radius)
