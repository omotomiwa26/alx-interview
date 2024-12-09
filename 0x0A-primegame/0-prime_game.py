#!/usr/bin/python3

"""
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a
    prime number from the set and removing that number and its multiples
    from the set.
    The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """
        where x is the number of rounds and nums is an array of n
        Return: name of the player that won the most rounds
        If the winner cannot be determined, return None
        You can assume n and x will not be larger than 10000
        You cannot import any packages in this task
    """
    if not nums or x < 1:
        return None

    # Step 1: Precompute primes up to the maximum number in nums
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Step 2: Count primes up to each n
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:  # Odd count means Maria wins
            maria_wins += 1
        else:  # Even count means Ben wins
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
