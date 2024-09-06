#!/usr/bin/python3
"""defines a square by: (based on 4-square.py) and adds print method"""


class Square(object):
    """A class that performs various actions related to a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ instantiation of the square class

        Args:
            size (int): size of the square
            position (tuple)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """calculates the current area of the square

        Returns:
            int: area of the square presntly

        """
        return self.__size ** 2

    @property
    def size(self):
        """returnsthe value of the square size

        setter methos raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        returns the positions
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the size of square to the stdout using `#`"""
        if self.__size == 0:
            print()
            return

        # Print the rows with leading spaces
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
