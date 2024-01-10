#!/usr/bin/python3
"""
This module creates a class `BaseGeometry` and adds certain functionalities.
"""


class BaseGeometry:
    """Takes up certain geometric operations

    Methods:
        area(self): A public instance method that raises an exception
                        when called
    """

    def area(self):
        """Raises an exception when called

        Raises:
            Exception: prints the message, "area() is not implemented"
        """

        raise Exception("area() is not implemented")
