#!/usr/bin/python3
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """Override == opeartor with !=."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with ==."""
        return self.real == value
