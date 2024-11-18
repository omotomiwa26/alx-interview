#!/usr/bin/python3
"""
    This function rotates an n X n 2D matrix
    in 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
        Rotates an n x n 2D matrix 90 degrees
        clockwise in-place.
            Args:
                matrix (list of list of int): The matrix to rotate.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for x in range(n):
        for y in range(x + 1, n):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    # Step 2: Reverse each row to achieve a 90-degree clockwise rotation
    for row in matrix:
        row.reverse()
