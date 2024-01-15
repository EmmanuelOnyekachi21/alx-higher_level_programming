#!/usr/bin/python3
""" This is a module for the Rectangle class """


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle's position.
            y (int): Y-coordinate of the rectangle's position.
            id (int): Identifier for the rectangle.

        Attributes:
            __width (int): Width of the rectangle.
            __height (int): Height of the rectangle.
            __x (int): X-coordinate of the rectangle's position.
            __y (int): Y-coordinate of the rectangle's position.
            id (int): Identifier for the rectangle.
        """

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """
            Getter for the width attribute.
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            Setter for the width attribute.

            Args:
                value (int): New value for the width.

            Raises:
                ValueError: If the value is not a positive integer.
            """
            if not isinstance(value, int) or value <= 0:
                raise ValueError("width must be >= 0")
            self.__width = width

        @property
        def height(self):
            """
            Getter for the height attribute.
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter for the height attribute.

            Args:
                value(int): New value for the height.

            Raises:
                ValueError: If the value is not a positive integer.
            """
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Height must be non-negative")
            self.__height = value

        @property
        def x(self):
            """
            Getter for the x attribute.
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            Setter for the x attribute.

            Args:
                value (int): New value for the x-coordinate.
            Raises:
                ValueError: If the value is not an integer.
            """
            if not isinstance(value, int) or value <= 0:
                raise ValueError("X-coordinate must be non-negative")
            self.__x = value

        @property
        def y(self):
            """
            Getter for the y attribute.
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            Setter for the y attribute.

            Args:
                value (int): New value for the y-coordinate.
            Raises:
                ValueError: If the value is not an integer.
            """
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Y-coordinate must be non-negative")
            self.__y = value
