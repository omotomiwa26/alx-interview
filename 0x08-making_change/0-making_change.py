#!/usr/bin/python3
"""
    Given a pile of coins of different values,
    This module determines the fewest number of coins
    needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
        Return: fewest number of coins needed to meet total
            If total is 0 or less, return 0
            If total cannot be met by any number of coins you have,
            return -1
        coins is a list of the values of the coins in your possession
        The value of a coin will always be an integer greater than 0
        You can assume you have an infinite number of each
        denomination of coin in the list
    """
    if total <= 0:
        return 0

    # Initialize dp array with a large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means total can't be made
    return dp[total] if dp[total] != float('inf') else -1
