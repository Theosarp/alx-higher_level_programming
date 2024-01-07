#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from dynamically creating new instance attributes
    except if it is called 'first_name'.
    """

    __slots__ = ["first_name"]
