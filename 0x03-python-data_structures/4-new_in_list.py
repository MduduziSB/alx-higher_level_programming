#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if len(my_list):
        cp_list = my_list[:]
        if idx > 0 and idx < len(cp_list):
            cp_list[idx] = element
        return cp_list
