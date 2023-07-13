#!/usr/bin/python3
"""
defines module that adds a new object
"""


def add_attribute(obj, name, attr_value):
    """adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, attr_value)
