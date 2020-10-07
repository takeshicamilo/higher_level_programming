#!/usr/bin/python3
""" read_lines.py """


def read_lines(filename="", nb_lines=0):
    """ read lines function """
    lines_number = 0
    with open(filename, encoding="utf-8") as a_file:
        for a_line in a_file:
            print("{}".format(a_line), end="")
            lines_number += 1
            if (lines_number == nb_lines):
                break
        print("")
