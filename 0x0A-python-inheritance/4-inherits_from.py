#!/usr/bin/python3
"""This module contains a single function that checks if an object
is only a subclass of another.
"""


def inherits_from(obj, a_class):
    """Checks if `obj` is a subclass only of `a_class`

    Args:
        obj (object): object to be checked if it is an instance
        a_class (class): class obj is compared with

    Returns:
        bool: True if obj is only a subclass of a_class, false otherwise

    """
    inst_check = type(obj) is a_class
    sub_check = isinstance(obj, a_class)
    return (not inst_check and sub_check)
