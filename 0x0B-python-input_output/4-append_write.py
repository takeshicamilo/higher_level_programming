#!/usr/bin/python3
""" append write """


def append_write(filename="", text=""):
    """ write file function """
    with open(filename, "a", encoding="utf-8") as file:
        length = file.write(text)
    return length
