#!/usr/bin/python3
"""
defines a module that creates an object a json file
"""
import json


def load_from_json_file(filename):
    """creates an object a json file"""
    with open(filename, encoding="utf-8") as MyFile:
        return json.load(MyFile)
