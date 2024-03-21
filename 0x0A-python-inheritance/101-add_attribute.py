#!/usr/bin/python3
"""This module has a function that adds a new attribute to an object"""


def add_attribute(obj, name, value):
    """Attempts to add a new attribute to the object.

    Args:
        obj: The object to add the attribute to.
        name: The name of the new attribute.
        value: The value to assign to the new attribute.

    Raise(s):
        TypeError: If the attempt to add a new_attribute isn't possible
        """
    if not hasattr(obj, name):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
