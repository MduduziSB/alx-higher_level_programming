#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        k = n + 1
        return (str[:n] + str[k:])
    return str
