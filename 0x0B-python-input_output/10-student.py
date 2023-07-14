#!/usr/bin/python3
"""defines a student class"""


class Student:
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list:
            count = 0
            for item in attrs:
                if type(item) == str:
                    count += 1
            if count == len(attrs):
                New_dict = {key: getattr(self, key)
                            for key in attrs if hasattr(self, key)}
                return New_dict
        return self.__dict__
