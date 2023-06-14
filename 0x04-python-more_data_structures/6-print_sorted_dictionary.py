#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for ky, value in sorted(a_dictionary.items()):
            print("{}: {}".format(ky, value))
    else:
        return None
