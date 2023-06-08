#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_sum = 0
    i = 1
    while (i < len(sys.argv)):
        total_sum += int(sys.argv[i])
        i += 1
    print("{}".format(total_sum))
