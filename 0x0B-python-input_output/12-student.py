#!/usr/bin/python3
""" students class """


class Student():
    """ class student """

    def __init__(self, first_name, last_name, age):
        """init function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json function"""
        if type(attrs) is not list:
            return self.__dict__
        for element in attrs:
            if type(element) is not str:
                return self.__dict__
        return {key: value for (key, value)
                in self.__dict__.items() if key in attrs}