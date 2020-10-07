#!/usr/bin/python3
""" inherits_ from """


def inherits_from(obj, a_class):
    """ inherits_from function """
    return(issubclass(type(obj), a_class) and not isinstance(obj, a_class))
