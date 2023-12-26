#!/usr/bin/python3
""" Defines a square class """


class Square:
    """ Class that defines a square.

    Attributes:
    __size (int): Private attribute representing the size of the square.

    Methods:
    __init__(self, size=0): Initializes a Square instance with a given size.
    area(self): Public instance method that returns the current square area.
    size(self): Getter method to retrieve the size attribute
    size(self, value): Setter method to set the size attribute
    my_print(self): Public instance method that prints in stdout the square with the character '#'
    """
    def __init__(self, size=0):
        """Initializes a Square instance with a given size
        Args:
            size (int): The size of the square.

            Raises:
                TypeError: if size is not an integer
                ValueError: if size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        """ Getter method to retrieve the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method to set the size attribute.

        Args:
            value(int): The size value to be set.
                Raises:
                    TypeError: If value is not an integer.
                    ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the area of a square

        Returns:
            int: area of the square presently
        """
        return self.__size ** 2

    def my_print(self):
        """ Public instance method that prints in stdout the square with the character '#' """
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
          print(self.__size * '#')
