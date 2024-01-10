#!/usr/bin/python3
"""
This module returns a True or False depending on if the
object is an instance of a class that 
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class that inherited
    from the specified class.

    Args:
        obj: An object to check for inheritance.
        a_class: The class to check for inheritance from.

    Returns:
        bool: True if the object is an instance of a class inherited 
                from the specified class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
