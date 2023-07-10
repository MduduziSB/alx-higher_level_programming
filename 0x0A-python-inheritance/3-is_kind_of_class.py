#!/usr/bin/python3
"""This module is used to determines wheter an object
is an instance of a specified class or not"""


def is_kind_of_class(obj, a_class):
    """Determines if an object is an instance of, or if the object is a
    n instance of a class that inherited from, the specified class"""

    return isinstance(obj, a_class)
