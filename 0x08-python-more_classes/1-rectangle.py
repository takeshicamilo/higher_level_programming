#!/usr/bin/python3
""" 1-rectangle """


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ init method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width retrieve """
        return self.__width

    @width.setter
    def width(self, value):
        """ width method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height retrieve """
        return self.__height

    @height.setter
    def height(self, value):
        """ height method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
