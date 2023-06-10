#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = 0, 0
    b1, b2 = 0, 0
    if len(tuple_a) <= 1:
        if (tuple_a):
            a1 = tuple_a[0]
    else:
        a1, a2 = tuple_a[0], tuple_a[1]
    if len(tuple_b) <= 1:
        if (tuple_b):
            b1 = tuple_b[0]
    else:
        b1, b2 = tuple_b[0], tuple_b[1]
    return (a1 + b1, a2 + b2)
