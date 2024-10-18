#!/usr/bin/python3
"""
    This module, In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste.
    Given a number n, write a method that calculates the fewest number of
    operations
    needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
        Prototype: def minOperations(n)
        Returns an integer
        If n is impossible to achieve, return 0
    """
    if n < 2:
        return 0  # No operations needed for n < 2

    operations = 0
    factor = 2  # Start with the smallest prime factor

    while n > 1:
        while n % factor == 0:
            operations += factor  # Increment operations by the factor value
            n //= factor  # Divide n by the factor

        factor += 1  # Move to the next potential factor

    return operations
