#!/usr/bin/python3
"""Document"""
import json

def save_to_json_file(my_obj, filename):
    """Document"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
