#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """ write file function """
    length = len(text)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return length
