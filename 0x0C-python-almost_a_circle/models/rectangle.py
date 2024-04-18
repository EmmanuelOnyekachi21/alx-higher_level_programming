#!/usr/python3

from models.base import Base
"""
This module defines the Rectangle class.

The Rectangle class inherits from the BAse class and represents a geometric
rectangle.

It encapsulates attributes such as:

width, height, x-coordinate, and y-coordinate.
"""


class Rectangle(Base):
    """
    Represemtation of a rectangle in the xy-plane.

    Attrbutes:
        width (int):        The width of the rectangle.
        height (int):       The height of the rectangle.
        x (int):            The x-coordinate.
        y (int):            The y-coordinate.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int):        The width of the rectangle.
            height (int):       The height of the rectangle.
            x (int):            The x-coordinate.
            y (int):            The y-coordinate.
            id (int):           Unique identifier of the rectangle.

        Returns:
            None
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
