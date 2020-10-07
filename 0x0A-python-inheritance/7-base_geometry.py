#!/usr/bin/python3

"""
A module for BaseGeometry class.
"""


class BaseGeometry():
    """A BaseGeometry class."""

    def integer_validator(self, name, value):
        """A method that validates value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """A method that raises an exception."""
        raise Exception("area() is not implemented")
