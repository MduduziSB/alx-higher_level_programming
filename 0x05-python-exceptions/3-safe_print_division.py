#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = a/b
    except (ZeroDivisionError, TypeError):
        value = None
    finally:
        print("{}".format(value))
    return value
