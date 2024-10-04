#!/usr/bin/python3


"""
    This module contains the function that
    returns a list of lists of integers
    representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
        Returns an empty list if n <= 0
        You can assume n will be always an integer
    """
    if n <= 0:
        return []

    pas_triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Each number is the sum of the two numbers directly above it
            row.append(pas_triangle[i-1][j-1] + pas_triangle[i-1][j])
        row.append(1)  # Last element of each row is always 1
        pas_triangle.append(row)

    return pas_triangle
