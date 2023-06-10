#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list):
        new_list = my_list[:]
        for idx in range(len(new_list)):
            if my_list[idx] % 2 == 0:
                new_list[idx] = 1
            else:
                new_list[idx] = 0
        return new_list
    return None
