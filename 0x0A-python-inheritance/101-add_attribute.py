#!/usr/bin/python3
"""Adds a new attribute to an object if it’s possible."""


def add_attribute(obj, att, value):
    """ TypeError exception: If the attribute cannot be added."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
