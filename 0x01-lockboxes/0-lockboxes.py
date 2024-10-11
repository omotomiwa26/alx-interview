#!/usr/bin/python3


"""
    This module contains the function that
    solves a lockbox algorithm
"""


def canUnlockAll(boxes):
    """
        boxes is a list of lists
        A key with the same number as a box opens that box
        You can assume all keys will be positive integer

            There can be keys that do not have boxes
        The first box boxes[0] is unlocked
        Return True if all boxes can be opened, else return False
    """
    n = len(boxes)
    unlocked = set([0])  # Start with box 0 unlocked
    keys = set(boxes[0])  # Get keys from box 0

    # Continue unlocking as long as we get new keys
    while keys:
        new_key = keys.pop()  # Take a key from the set

        # Valid key and box not already unlocked
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)  # Unlock the box
            keys.update(boxes[new_key])  # Add new keys from this box

    return len(unlocked) == n
