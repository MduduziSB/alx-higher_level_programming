#!/usr/bin/python3
"""Module that determines whether an object is an instance of a class that"""
"""inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Tells whether or not an object is an instance"""
    """or herited from the spacified type"""

    if type(obj) == a_class or isinstance(type(obj), a_class):
        return True
    return False
