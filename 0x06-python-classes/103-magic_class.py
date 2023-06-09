#!/usr/bin/python3
"""define MagicClass"""

import math


class MagicClass:
    """Defining attributes and methods"""

    def __init__(self, radius=0):
        """Initialisation of class attribute"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """Method to compute area"""
    def area(self):
        return (self.__radius ** 2 * math.pi)

    """Method used to compute circumference"""
    def circumference(self):
        return (2 * math.pi * self.__radius)
