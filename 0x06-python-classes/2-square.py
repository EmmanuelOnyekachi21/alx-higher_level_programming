#!/usr/bin/python3
""" Defines a square class """


class Square:
    """ Class that defines a square.

    Attributes:
    __size (int): Private attribute representing the size of the square.

    Methods:
    __init__(self, size=0):
        initializes a Square instance with a given size.
    """
    def __init__(self, size=0):
        """Initializes a Square instance with a given size
        Args:
            size (int): The size of the square.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
