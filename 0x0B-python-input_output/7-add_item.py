#!/usr/bin/python3
"""
This module adds all argument to a Python list and then save them to a file.
"""



import sys
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

# Checks if the file exists, and create it if it doesn't
if not path.exists(filename):
    save_to_json_file([], filename)

# Load the current list from the file
my_list = load_from_json_file(filename)

my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
