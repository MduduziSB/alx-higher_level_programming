#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dic2 = {'IX': 9, 'IV': 4, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    if roman_string is not None and isinstance(roman_string, str):
        integer = 0
        i = 0
        while i < (len(roman_string)):
            check = 0
            if i+1 < len(roman_string) and roman_string[i: i+2] in dic2:
                integer += dic2[roman_string[i: i+2]]
                i += 2
                check = 1
            if check == 0:
                integer += dic[roman_string[i]]
                i += 1
        return integer
    return 0
