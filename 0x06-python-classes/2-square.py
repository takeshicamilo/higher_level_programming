#!/usr/bin/python3
"""Class square 2"""


class Square:
    """ init process """
    def __init__(self, size=0):
        """ initialize method

        Args:
            size(int): Size of square
        Returns: none
        """

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
