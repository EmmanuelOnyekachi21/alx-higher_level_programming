#!/usr/bin/python3
"""This module contains a definition of the BaseGeometry class"""


class BaseGeometry(object):
    """This is a class that serve as the base class for geometric shapes

    it has two methods defined as "area" which raises an exception as its
    definition would be implemented by various subclasses and
    "integer_validator" which validates a value.

    """
    def area(self):
        """Raises an exception as this method is to be overwritten later

        Raises:
            Exception: always raises this exception

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is of the right input

        Raises:
            TypeError: if value is not an int
            ValueError: if value is equal to or less than 0

        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
