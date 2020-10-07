#!/usr/bin/python3
""" inherits_ from """


def inherits_from(obj, a_class):
    """ inherits_from function """
    if issubclass(a_class, a_class) == obj:
        return True
    else:
        return False
