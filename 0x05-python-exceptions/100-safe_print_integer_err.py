#!/usr/bin/python3
"""
prints an integer.
"""


def safe_print_integer_err(value):
    """
    Entry point.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e),  file=sys.stderr)
        return False
