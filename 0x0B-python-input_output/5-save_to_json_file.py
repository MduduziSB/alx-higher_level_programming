#!/usr/bin/python3
"""Defines a module that writes object to a text file using json"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using json"""
    with open(filename, "w", encoding="utf-8") as MyFile:
        json.dump(my_obj, MyFile)
