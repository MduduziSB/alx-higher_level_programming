#!/usr/bin/python3
for i in range(9):
    j = i + 1
    while (j < 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
        j += 1
