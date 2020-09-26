#!/usr/bin/python3
def print_square(size):
    if type(size) is int:
        if size < 0:
            raise ValueError("size must be >= 0")
        for _i in range(size):
            for _x in range(size):
                print("#", end="")
            print("")
    else:
        raise TypeError("size must be an integer")
