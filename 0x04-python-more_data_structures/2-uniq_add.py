#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is not None:
        uniq_sum = 0
        for i in range(len(my_list)):
            check = 0
            for j in range(i):
                if my_list[i] == my_list[j]:
                    check += 1
                    break
            if check == 0:
                uniq_sum += my_list[i]
        return uniq_sum
    return None
