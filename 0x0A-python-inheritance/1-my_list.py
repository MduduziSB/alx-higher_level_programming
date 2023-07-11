#!/usr/bin/python3
"""
Module that creates MyList class
"""


class MyList(list):
    """This is class MyList that inherits from list class"""

    def print_sorted(self):
        """prints a list in an ascending order"""
        print(sorted(self))
