#!/usr/bin/python3
"""
executes a function safely.
"""


import sys


def safe_function(fct, *args):
    """
    Entry point.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e),  file=sys.stderr)
        return None
