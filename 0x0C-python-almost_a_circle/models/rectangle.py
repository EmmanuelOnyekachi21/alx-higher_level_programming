#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class inherits from the BAse class and represents a geometric
rectangle.

It encapsulates attributes such as:

width, height, x-coordinate, and y-coordinate.
"""

from models.base import Base


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x
        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y
        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
