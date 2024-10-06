#!/usr/bin/python3
"""
Pascal triangle module
"""


def pascal_triangle(n):
    """
    Pascal triangle
    """
    if n <= 0:
        return []
    triangle = []
    c = 1
    while (c <= n):
        row = [1] * c
        if c <= 2:
            triangle.append(row)
            c += 1
        else:
            for i in range(len(triangle[-1]) - 1):
                row[1 + i] = triangle[-1][i] + triangle[-1][i + 1]
            triangle.append(row)
            c += 1

    return triangle
