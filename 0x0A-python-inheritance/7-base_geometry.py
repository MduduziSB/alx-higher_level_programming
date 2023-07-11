#!/usr/bin/python3
"""
Module that creates a class called BaseGeometry
"""


class BaseGeometry:
    """Class that raises an Exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validation method"""
        if type(value) != int:
            raise TypeError(name + ' ' + "must be an integer")
        if value <= 0:
            raise ValueError(name + ' ' + "must be greater than 0")
