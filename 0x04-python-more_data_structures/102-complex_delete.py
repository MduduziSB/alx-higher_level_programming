#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is not None:
        for i in a_dictionary.copy():
            if a_dictionary[i] == value:
                del a_dictionary[i]
        return a_dictionary
