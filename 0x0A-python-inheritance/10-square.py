#!/usr/bin/python3
"""Inherits from Rectangle class as defined in 9-base_geometry.py"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle as defined in 9-base_geometry.py

    this class defines a subclass of Rectangle and
    it's instantiation

    Attributes:
        _size (int): size of square

    """
    def __init__(self, size):
        """Instantiates Square subclass

        Args:
            size (int): size of Square instance

        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
