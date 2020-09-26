#!/usr/bin/python3
"""say_my_name"""


def say_my_name(first_name, last_name=""):
    """ say my name function"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    first_name += " " + last_name
    print("My name is", first_name)
