#!/usr/bin/python3
""" 2-rectangle.py """


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ init method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width method """
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
        """ height method """
        return self.__height

    @height.setter
    def height(self, value):
        """ height method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area method """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ perimeter method """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter
        a = 2 * self.__width
        b = 2 * self.__height
        perimeter = a + b
        return perimeter

    def __str__(self):
        """ string creation """
        string = ""
        if self.height == 0 or self.width == 0:
            return string
        string = (('#' * self.__width) + '\n') * self.__height
        string = string[:-1]
        return string

    def __repr__(self):
        """ repr method """
        return ("Rectangle ({:d}, {:d})".format(self.__width, self.__height))
