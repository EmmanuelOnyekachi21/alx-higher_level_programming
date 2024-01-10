#!/usr/bin/python3
"""Inherits from BaseGeometry class as defined in 7-base_geometry.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry as defined in 7-base_geometry.py

    this class defines a subclass of BaseGeometry; `Rectangle` and
    it's instantiation

    Attributes:
        __width (int): Width of rectangle
        __height (int): height of rectangle

    """
    def __init__(self, width, height):
        """Instantiates rectangle subclass

        Args:
            width (int): width of rectangle instance
            height (int): height of rectangle instance

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns the string represntation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of the Rectangle instance"""
        return self.__width * self.__height
