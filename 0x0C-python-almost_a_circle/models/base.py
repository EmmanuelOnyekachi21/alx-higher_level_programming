#!/usr/bin/python3
"""
This module defines the Base class.

The Base class serves as the base class for all other classes in this project.
It manages the 'id' attribute for all future classes,
and avoids duplicating code.
"""
import json


class Base:
    """
    The Base class for managing the id attribute.

    Attribute(s):
        __nb_objects: private class attibute; initialized to 0.
        id (int): A public instance attribute; reps the id of the object.
    Method(s):
        __init__(self, id=None): The method that initializes the Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base object.

        Args:
            id (int, optional): The id of the object.
                                If None, it is auto-generated.
        Returns:
            None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of 'list_dictionaries'

        Return: JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
