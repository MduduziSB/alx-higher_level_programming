#!/usr/bin/python3
def uppercase(str):
    for k in str:
        if ord(k) >= 97 and ord(k) <= 122:
            i = ord(k) - 32
        else:
            i = ord(k)
        print("{}" .format(chr(i)), end="")
    print()
