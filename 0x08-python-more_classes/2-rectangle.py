#!/usr/bin/python3
""" This is a rectangle module"""


class Rectangle:
    """
    This class defines a Rectangle.

    Attributes:
        __width(int): The width of the Rectangle
        __height(int): The height of the Rectangle

    Methods:
        width (property): Retrieve the width of the Rectangle
        height (property): Retrieves the height of the Rectangle
        width (setter): Sets the width of the Rectangle
        height (setter): Sets the height of the Rectangle
        __init__(self, width=0, height=0): Instantiate Rectangle object.
        """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with optional width and height.

        Args:
            width(int): The width of the Rectangle (default 0).
            height(int): The height of the Rectangle (default 0).
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of a Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
