#!/usr/bin/python3
""" 4-print_square.py """


def print_square(size):
    """ print square """
    if type(size) is int:
        if size < 0:
            raise ValueError("size must be >= 0")
        for _i in range(size):
            for _x in range(size):
                print("#", end="")
            print("")
    else:
        raise TypeError("size must be an integer")
