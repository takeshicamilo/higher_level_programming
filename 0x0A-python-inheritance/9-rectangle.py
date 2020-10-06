#!/usr/bin/python3
""" Class Base geometry """


class BaseGeometry:
    """ Base geometry """

    def area(self):
        """ area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator """

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value is 0 or value < 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ init function """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """ str """

        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """ area function """

        return self.__width * self.__height
