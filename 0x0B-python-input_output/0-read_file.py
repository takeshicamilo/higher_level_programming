#!/usr/bin/python3
""" read_file """


def read_file(filename=""):
    """ read file function """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
