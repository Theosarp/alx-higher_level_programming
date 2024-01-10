#!/usr/bin/python3
"""Pascal’s triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
     representing the Pascal’s triangle of n:
     """
      rows = [[1 for y in range(x + 1)] for x in range(n)]
    for n in range(n):
        for x in range(n - 1):
            rows[n][x + 1] = sum(rows[n - 1][x:x + 2])
    return rows
