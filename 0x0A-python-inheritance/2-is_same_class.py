#!/usr/bin/python3
"""This module contains a single function that checks if an object
is an instance of another.
"""


def is_same_class(obj, a_class):
    """Checks if `obj` is an instance of `a_class`

    Args:
        obj (object): object to be checked if it is an instance
        a_class (class): class obj is compared with

    Returns:
        bool: True if obj is an instance of a_class, false otherwise

    """
    return (type(obj) == a_class)
