#!/usr/bin/python3
"""Defines a file that writes in a file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as MyFile:
        nchars = MyFile.write(text)
    return nchars
