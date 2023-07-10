#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Tells whether or not an object is an instance"""
    """or herited from the spacified type"""
    if type(obj) == a_class or isinstance(type(obj), a_class):
        return True
    return False
