#!/usr/bin/python3
"""This module is used to determines wheter an object
is an instance of a specified class or not"""


def is_same_class(obj, a_class):
    """Determines if an object is an instance of specified class"""
    if type(obj) == a_class:
        return True
    return False
