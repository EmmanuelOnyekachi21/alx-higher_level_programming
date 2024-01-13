#!/usr/bin/python3
"""
This module houses a function that writes an Object to a text file, using JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This fxn writes an Object to a text file, using a JSON representation

    Args:
        my_obj: Object to be written
        filename: File name where object would be stored.

    Returns:

    """
    with open(filename, "w", encoding="UTF-8") as file:
        bytes_written = file.write(json.dumps(my_obj))
    return bytes_written
