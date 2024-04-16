#!/usr/bin/python3
"""Document modules"""
import json
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
items = load(filename)
if not filename:
    items =[]
else:
    items += (sys.argv[1:])
    save(items, filename)
