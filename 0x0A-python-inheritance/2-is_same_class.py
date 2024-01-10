#!/usr/bin/python3
"""
This module checks if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object is exactly an instance of the specified class.

    Args:
        obj: An object to check for its instance.
        a_class: The class to compare the object's instance with

    Returns:
        bool: True if the object is an instance of the specified class,
                otherwise False.
    """
    if type(obj) == a_class:
        return True

    return False
