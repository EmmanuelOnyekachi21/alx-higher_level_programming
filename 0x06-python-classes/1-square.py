#!/usr/bin/python3
""" Defines a square class """


class Square:
    """ Class that defines a square.

    Attributes:
    __size (int): Private attribute representing the size of the square.

    Methods:
    __init__(self, size):
        initializes a Square instance with a given size.
    """
    def __init__(self, size):
        """Initializes a Square instance with a given size
        Args:
            size (int): The size of the square.
        """
        self.__size = size
