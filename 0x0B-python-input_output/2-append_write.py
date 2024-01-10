#!/usr/bin/python3
"""Appends a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file(UTF8)
     returns the number of characters added
     """

    with open(filename, "a") as file:
        file.write(text)
    return len(text)
