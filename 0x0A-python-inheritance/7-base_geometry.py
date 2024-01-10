#!/usr/bin/python3
"""
This module creates a class `BaseGeometry` and adds certain functionalities.
"""


class BaseGeometry:
    """Takes up certain geometric operations

    Methods:
        area(self): A public instance method that raises an exception
                        when called
        integer_validator(self, name, value): validates value.
    """

    def area(self):
        """Raises an exception when called

        Raises:
            Exception: prints the message, "area() is not implemented"
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates Value.

        Args:
            name: Always a string
            value: Value to be validated.

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")

        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
