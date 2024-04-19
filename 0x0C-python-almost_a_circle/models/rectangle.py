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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle instance.

        Args:
            None.

        Return:
            Area of the Rectangle class.
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character, `#`
        """
        for _ in range(self.y):
            print("{}".format('\n'), end="")

        for _ in range(self.height):
            for _ in range(self.x):
                print("{}".format(' '), end="")
            print('#' * self.width)

        # A better way would be:
        # print('\n' * self.y, end="")
        # for _ in range(self.height):
        #    print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        The string representation includes information about the Rectangle's 
        attributes, such as its ID, position (x, y), width, and height.

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return (
                f"[{Rectangle.__name__}] "
                f"({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}/{self.height}"
                )

    def update(self, *args):
        """
        Assigns arguments to the attributes of the Rectangle instance.

        Args:
            *args: Variable number of arguments in the following order:
                1st: id
                2nd: width
                3rd: height
                4th: x
                5th: y

        Returns:
            None
        """
        for arg in args:
            self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]

