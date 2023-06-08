#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)
    if nargs == 1:
        print("{} arguments.".format(nargs - 1))
    else:
        if nargs == 2:
            print("{} argument:".format(nargs - 1))
        else:
            print("{} arguments:".format(nargs - 1))
        for i in range(1, nargs):
            print("{}: {}".format(i, sys.argv[i]))
