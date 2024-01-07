#!/usr/bin/python3
""" This module prints a square with the character '#'."""

def print_square(size):
    """
    This module prints a square with the character '#'.

    args:
        size: This is the size length of the square.

    raises:
        TypeError: if size isn't an integer.
                 : if size is a float.
        ValueError: if size < 0
    """
    print_symbol = "#"

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for _ in range(size):
        print(print_symbol * size)
