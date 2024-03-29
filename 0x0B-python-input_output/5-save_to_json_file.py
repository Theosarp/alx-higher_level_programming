#!/usr/bin/python3
"""Writes an Object"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w") as file:
        content = json.dumps(my_obj)
        file.write(content)
