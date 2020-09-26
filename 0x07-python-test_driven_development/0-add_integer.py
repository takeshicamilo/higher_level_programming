#!/usr/bin/python3
"""
0-add_integer

"""


def add_integer(a, b=98):
    """
    add_integer
    Args:
        a (int, optional): number
        b (int, optional): Defaults to 98.
    Returns:
        temp : add
    """
    tempA = a
    tempB = b
    if (type(tempA)is not int and type(tempA)is not float):
        raise TypeError("a must be an integer")
    if (type(tempB)is not int and type(tempB)is not float):
        raise TypeError("b must be an integer")
    if (type(tempA) is float):
        tempA = int(a)
    if (type(tempB) is float):
        tempB = int(b)
    temp = tempA + tempB
    return temp
