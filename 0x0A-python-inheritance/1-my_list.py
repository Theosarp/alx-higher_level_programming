#!/usr/bin/python3
"""a class that inherits from list."""


class MyList(list):
    """class methods and attributes."""

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
