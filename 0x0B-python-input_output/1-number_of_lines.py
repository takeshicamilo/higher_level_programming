#!/usr/bin/python3
""" 1-number_of_lines """


def number_of_lines(filename=""):
    """ number of lines function """
    lines_number = 0

    with open(filename, encoding="utf-8") as a_file:
        for a_line in a_file:
            lines_number += 1
    return lines_number
