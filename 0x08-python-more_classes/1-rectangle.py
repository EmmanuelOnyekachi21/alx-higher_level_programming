#!/usr/bin/python3
""" 1. Real definition of a rectangle."""


class Rectangle:
    """Defines a rectangle

    Methods:
        __init__(self, width, height): Initilaizes the width and height.

    Raises:
        ValueError: if height is >= 0
        TypeError: Height must be an integer.

    """
    def __init__(self, width=0, height=0):
        """Initializzes the width and height."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

