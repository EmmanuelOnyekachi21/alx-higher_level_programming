#!/usr/bin/python3
import json
""" To JSON string """


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object (string)

    Args:
        obj: An object(string)

    Returns:
        json_written: The JSON representation of `my_obj`
    """

    json_written = json.dumps(my_obj)

    return json_written
