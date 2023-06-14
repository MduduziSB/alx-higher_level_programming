#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary is not None:
        num_keys = 0
        for k, s in a_dictionary.items():
            num_keys += 1
        return num_keys
    return None
