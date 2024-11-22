#!/usr/bin/python3
"""
This module defines a function that rotates a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    """
    n = len(matrix)

    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[i][j], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()  # reverse each row
