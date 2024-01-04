#!/usr/bin/python3
""" This module takes on the Addition operation of two digits"""


def add_integer(a, b=98):

    """ Adds two digits

    Args:
        a (int or float): An integer involved in the operation.
        b (int or float): Default value of 98.

    Raises:
        TypeError: raises error if a args is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    else:
        a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return a + b
