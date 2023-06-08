#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)
    total_sum = 0
    i = 1
    while (i < nargs):
        total_sum += int(sys.argv[i])
        i += 1
        print("{}".format(total_sum))
