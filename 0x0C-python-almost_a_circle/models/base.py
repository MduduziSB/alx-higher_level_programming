#!/usr/bin/python3
"""
deifines a class called Base
"""
import json
import os
import csv


class Base:
    """class Base definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initilization method of Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        that returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                cont_list = [elem.to_dictionary() for elem in list_objs]
                myFile.write(Base.to_json_string(cont_list))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if dictionary is not None and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                class_ins = cls(1, 1)
            if cls.__name__ == "Square":
                class_ins = cls(1)
            class_ins.update(**dictionary)
            return class_ins

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        fname = str(cls.__name__) + ".json"
        if os.path.exists(fname):
            with open(fname, encoding="utf-8") as myFile:
                new_list = Base.from_json_string(myFile.read())
                return [cls.create(**elem) for elem in new_list]
        return []
