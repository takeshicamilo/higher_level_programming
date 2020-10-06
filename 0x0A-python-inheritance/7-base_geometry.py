#!/usr/bin/python3
""" Class Base geometry """


class BaseGeometry:
    """ Base geometry """

    def area(self):
        """ area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator """

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value is 0 or value < 0:
            raise ValueError("<name> must be greater than 0")
