#!/usr/bin/python3
"""A module on using both load_json and save_json"""

import json
import sys

save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file
arguments = sys.argv[1:]
# print(arguments)

filename = "add_item.json"

try:
    items = load_json(filename)
except FileNotFoundError:
    items = []

items.extend(arguments)
save_json(items, filename)
