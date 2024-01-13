#!/usr/bin/python3
"""
This module houses a fxn that creates an Object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    This fxn creates an object from a `JSON` file

    Args:
        filename: JSON file

    Return:

    """
    with open(filename, "r", encoding="UTF-8") as file:
        file_content = json.load(file)
    return file_content
