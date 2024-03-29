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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
            TypeError: If not an integer
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

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
            TypeError: If not an integer
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
            TypeError: If value is not an integer.
            ValueError: If the value is not > 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
            TypeError: If the value is not an integer.
            ValueError: If y is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints, in stdout, the rectangle instance with the character '#'
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}"
                )

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        attribute_class = ['id', 'width', 'height', 'x', 'y']

        if args:
            for attribute, value in zip(attribute_class, args):
                setattr(self, attribute, value)
        elif kwargs:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)
