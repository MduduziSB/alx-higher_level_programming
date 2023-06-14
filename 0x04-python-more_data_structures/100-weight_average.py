#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        prod = 0
        tot_weight = 0
        for i in my_list:
            prod += i[0]*i[1]
            tot_weight += i[1]

        return ((float(prod))/tot_weight)
    return 0
