#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 == 0:
        k = i + 32
    else:
        k = i
    print("{}" .format(chr(k)), end="")
