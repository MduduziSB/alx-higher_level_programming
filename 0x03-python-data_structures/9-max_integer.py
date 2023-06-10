#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in range(1, len(my_list)):
        if i == 1:
            max = my_list[0]
        if max < my_list[i]:
            max = my_list[i]
    return max
