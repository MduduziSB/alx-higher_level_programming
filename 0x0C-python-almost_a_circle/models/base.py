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
        if json_string is None or json_string == []:
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
            with open(fname, "r", encoding="utf-8") as myFile:
                new_list = Base.from_json_string(myFile.read())
                return [cls.create(**elem) for elem in new_list]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv file"""
        filename = cls.__name__ + ".CSV"
        name = cls.__name__
        with open(filename, "w", newline="") as mycsv:
            if list_objs is None or list_objs == []:
                mycsv.write("[]")
            else:
                if name == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if name == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                thewriter = csv.DictWriter(mycsv, fieldnames=fieldnames)
                for to_dic in list_objs:
                    thewriter.writerow(to_dic.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".CSV"
        name = cls.__name__
        if not os.path.exists(filename):
            return []
        with open(filename, "r", newline="") as mycsv:
            if name == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            if name == "Square":
                fieldnames = ["id", "size", "x", "y"]
            dic = csv.DictReader(mycsv, fieldnames=fieldnames)
            dic = [dict([x, int(y)] for x, y in z.items()) for z in dic]
            return [cls.create(**z) for z in dic]
