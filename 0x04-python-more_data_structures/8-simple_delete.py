#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        for i in a_dictionary:
            if i == key:
                del a_dictionary[i]
                break
        return a_dictionary
    return None
