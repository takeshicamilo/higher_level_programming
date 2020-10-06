#!/usr/bin/python3
""" My_list class """


class MyList(list):
    """ My lists class"""

    def print_sorted(self):
        """ print_sorted function """
        print(sorted(self))
