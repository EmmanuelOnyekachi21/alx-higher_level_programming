#!/usr/bin/python3
"""This module contains a single function that checks if an object
is an instance or subclass of another.
"""


def is_kind_of_class(obj, a_class):
    """Checks if `obj` is an instance or subclass of `a_class`

    Args:
        obj (object): object to be checked if it is an instance
        a_class (class): class obj is compared with

    Returns:
        bool: True if obj is an instance/subclass a_class, false otherwise

    """
    return (isinstance(obj, a_class))
