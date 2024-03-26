#!/usr/bin/python3
"""Documentation"""


def class_to_json(obj):
    """
    Converts attributes of a class instance to dictionary for JSON
    serialization

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing the serializable attributes of an object
    """
    output = {}

    # Iterate through object attributes.
    for attr, value in obj.__dict__.items():
        # Check for Valid data types for JSON
        if isinstance(value, (list, dict, str, int, bool)):
            output[attr] = value
    return output
