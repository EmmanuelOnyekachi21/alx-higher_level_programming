#!/usr/bin/python3
"""This is a Base class"""


class Base:
    """
    Base class for managing unique identifiers in other classes.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the
                            number of objects created from Base class.
        id (int): A public instance attribute representing the unique
                    identifier assigned to each instance.

    Methods:
        __init__(self, id=None): Constructor method for Base class.
            Parameters:
                id (int): Optional unique identifier. If not provided,
                          a new id is generated based on __nb_objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Parameters:
            id (int): Optional unique identifier. If not provided,
                      a new id is generated based on __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
