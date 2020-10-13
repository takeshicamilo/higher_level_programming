#!/usr/bin/python3
""" rectangle class """

from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init function """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ str method """

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        """ getter method """

        return self.__width

    @width.setter
    def width(self, width):
        """ setter method """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter method """

        return self.__height

    @height.setter
    def height(self, height):
        """ setter method """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter method """

        return self.__x

    @x.setter
    def x(self, x):
        """ setter method """

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter method """

        return self.__y

    @y.setter
    def y(self, y):
        """ setter method """

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ area method """

        return self.__height * self.__width

    def display(self):
        """ display method """

        for _i in range(self.__y):
            print("")
        for _i in range(self.__height):
            for _x in range(self.__x):
                print(" ", end="")
            for _x in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """ update method """

        i = 0
        if len(args) != 0:
            for argv in args:
                if i == 0:
                    self.id = argv
                if i == 1:
                    self.__width = argv
                if i == 2:
                    self.__height = argv
                if i == 3:
                    self.__x = argv
                if i == 4:
                    self.__y = argv
                i += 1
        else:
            keys = kwargs.keys()
            for i in keys:
                if i == "id":
                    self.id = kwargs["id"]
                if i == "width":
                    self.width = kwargs["width"]
                if i == "height":
                    self.height = kwargs["height"]
                if i == "x":
                    self.x = kwargs["x"]
                if i == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """ dictionary method """

        new_dictionary = {}
        new_dictionary["id"] = self.id
        new_dictionary["width"] = self.width
        new_dictionary["height"] = self.height
        new_dictionary["x"] = self.x
        new_dictionary["y"] = self.y
        return new_dictionary
