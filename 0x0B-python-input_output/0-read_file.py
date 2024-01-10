#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
