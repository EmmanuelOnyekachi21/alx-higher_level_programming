#!/usr/bin/python3
"""This contains a sinle function "lookup" that returns a list of
attributes and methods within a class.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
