#!/usr/bin/python3
"""
This module checks if object is an instance or an instance inherited from a
specified class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if object is an instance or an instance inherited from a
    specified class

    Args:
        obj: Object
        a_class: A class

    Returns:
        bool: Either true or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
