#!/usr/bin/python3
"""Module that defines a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definitioon"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square class __init__ method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, w_value):
        """setter method"""
        self.width = w_value
        self.height = w_value

    def update(self, *args, **kwargs):
        """update class attributes"""
        list_attr = ["id", "size", "x", "y"]
        if args is not None and len(args) != 0:
            for idx, value in enumerate(args):
                if idx == 0:
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.size, self.x, self.y)
                elif idx == 1:
                    self.size = value
                elif idx == 2:
                    self.x = value
                else:
                    self.y = value

        list_attr = ["size", "x", "y", "id"]
        if args is None or len(args) == 0 and len(kwargs) != 0:
            for attr_name in list_attr:
                if attr_name in kwargs:
                    if attr_name == "id" and kwargs.get(attr_name) is not None:
                        self.id = kwargs.get(attr_name)
                    if attr_name == "id" and kwargs.get(attr_name) is None:
                        self.__init__(self.size, self.x, self.y)
                    if attr_name == "size":
                        self.size = kwargs.get(attr_name)
                    if attr_name == "x":
                        self.x = kwargs.get(attr_name)
                    if attr_name == "y":
                        self.y = kwargs.get(attr_name)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """overloaded __str__ method definition"""
        str1 = f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        return str1
