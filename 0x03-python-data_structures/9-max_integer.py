#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        max = my_list[0]
        i = 1
        while (i < len(my_list)):
            if max < my_list[i]:
                max = my_list[i]
            i += 1
        return max
    return None
