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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherits from Base.

        Returns: None.
        '''
        if list_objs is None:
            list_objs = []
        filename = f'{cls.__name__}.json'
        with open(filename, "w") as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation

        Args:
            json_string: a string representing a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        # Parse the JSON string into a list of dictionaries
        dict_list = json.loads(json_string)
        return dict_list

    @classmethod
    def create(cls, **dictionary):
        """
        Creates and returns an instance with all attributes already set
        from the given dictionary.

        Args:
            **dictionary (dict): A dictionary containing attribute-value pairs.

        Returns:
            Instance of the class with attributes set from the dictionary.
        """
        # Create a dummy instance.
        #dummy_instance = cls(1, 1)

        #dummy_instance.update(**dictionary)

        #return dummy_instance
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy
