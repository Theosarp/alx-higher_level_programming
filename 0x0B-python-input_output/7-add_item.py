#!/usr/bin/python3
"""Adds all arguments to a Python list,
and saves them to a file:
"""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []
    argv.pop(0)
    items.extend(argv)
    save_to_json_file(items, 'add_item.json')
