#!/usr/bin/python3
"""defines a square by: (based on 4-square.py) and adds print method"""


class Square(object):
    """A class that performs various actions related to a square"""
    def __init__(self, size=0):
        """ instantiation of the square class

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

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

    def my_print(self):
        """prints the size of square to the stdout using `#`"""
        index = 0

        while (self.__size > 0):
            for x in range(self.__size):
                print("#", end='')
            print()
            index += 1
            if index == self.__size:
                break
        else:
            print()
