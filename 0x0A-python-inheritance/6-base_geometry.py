#!/usr/bin/python3
"""This module contains a definition of the BaseGeometry class"""


class BaseGeometry(object):
    """This is a class that serve as the base class for geometric shapes

    it has only a method defined "area" which raises an exception as its
    definition would be implemented by various subclasses

    """
    def area(self):
        """Raises an exception as this method is to be overwritten later

        Raises:
            Exception: always raises this exception

        """
        raise Exception("area() is not implemented")
