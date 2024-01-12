#!/usr/bin/python3
"""4. From JSON string to Object """


import json


def from_json_string(my_str):
    """
    The function returns an object (Python DS) represented by a JSON string:

    Args:
        my_str: Python Data Structure object

    Returns:
        python_written: object (Python DS) represented by a JSON string
    """

    python_written = json.loads(my_str)
    return python_written
