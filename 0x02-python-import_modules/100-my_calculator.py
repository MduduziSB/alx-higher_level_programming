#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    oper = "+-*/"
    i = 0
    for j in oper:
        if sys.argv[2] == j:
            i += 1
            break
    if i == 0:
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        c = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if c == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        if c == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if c == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if c == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
    exit(1)
