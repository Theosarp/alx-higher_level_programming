#!/usr/bin/python3
"""Creates an Object"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename, "r") as file:
        content = json.loads(file.read())
    return content
