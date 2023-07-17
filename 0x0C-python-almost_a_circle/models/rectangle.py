#!/usr/bin/python3
"""
defines class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle init method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, w_value):
        """width setter method"""
        if type(w_value) != int:
            raise TypeError("width must be an integer")
        if w_value <= 0:
            raise ValueError("width must be > 0")
        self.__width = w_value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, h_value):
        """height setter method"""
        if type(h_value) != int:
            raise TypeError("height must be an integer")
        if h_value <= 0:
            raise ValueError("height must be > 0")
        self.__height = h_value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, x_value):
        """x setter method"""
        if type(x_value) is not int:
            raise TypeError("x must be an integer")
        if x_value < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, y_value):
        """y setter method"""
        if type(y_value) != int:
            raise TypeError("y must be an integer")
        if y_value < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_value

    def area(self):
        """computes an area of a rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y_cord in range(self.y):
            print()
        for row in range(self.height):
            for x_cord in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update class attributes"""
        list_attr = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) != 0:
            for idx, value in enumerate(args):
                if idx == 0:
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                elif idx == 1:
                    self.width = value
                elif idx == 2:
                    self.height = value
                elif idx == 3:
                    self.x = value
                else:
                    self.y = value

        if (args is None or len(args) == 0) and len(kwargs) != 0:
            list_attr = ["width", "height", "x", "y", "id"]
            for attr_name in list_attr:
                if attr_name in kwargs:
                    if attr_name == "id" and kwargs.get(attr_name) is not None:
                        self.id = kwargs.get(attr_name)
                    if attr_name == "id" and kwargs.get(attr_name) is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    if attr_name == "width":
                        self.width = kwargs.get(attr_name)
                    if attr_name == "height":
                        self.height = kwargs.get(attr_name)
                    if attr_name == "x":
                        self.x = kwargs.get(attr_name)
                    if attr_name == "y":
                        self.y = kwargs.get(attr_name)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "y": self.y, "x": self.x}

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        str1 = f"[Rectangle] ({self.id}) {self.x}/{self.y} "
        str2 = f"- {self.width}/{self.height}"
        return str1 + str2
