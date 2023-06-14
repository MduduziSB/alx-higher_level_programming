#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dic = {}
        for key, value in a_dictionary.items():
            new_dic[key] = 2 * value
        return new_dic
    return None
