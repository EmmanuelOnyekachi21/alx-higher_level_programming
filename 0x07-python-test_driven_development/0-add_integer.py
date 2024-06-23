#!/usr/bin/python3
"""
This module implements the add function.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting to integer).

    Parameters:
    a: The first integer or float.
    b: The second integer or float.

    Returns:
    The sum of a and b as an integer.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(a) != int and type(b) != float:
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return (a + b)
