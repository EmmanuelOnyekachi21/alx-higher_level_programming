#!/usr/bin/python3

"""
This module returns the list of available attributes and methods of an object
"""

def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    
    args:
        obj: An object.

    returns:
        a list object
    """

    print(dir(obj))
