#!/usr/bin/python3
"""Defines a module that appends a file"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as MyFile:
        nchars = MyFile.write(text)
    return nchars
