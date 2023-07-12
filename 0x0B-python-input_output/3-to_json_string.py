#!/usr/bin/python3
"""
defines a function that returns the JSON representation of an objec
"""
import json


def to_json_string(my_obj):
    """def to_json_string(my_obj)"""
    return json.dumps(my_obj)
