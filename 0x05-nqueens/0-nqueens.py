#!/usr/bin/python3
"""
    This program solves the N queens puzzle is the challenge
    of placing N non-attacking queens on an N×N chessboard.
"""

import sys


def N_queens(solution):
    """
        Usage: nqueens N

            If the user called the program with the wrong number of arguments,
            print Usage: nqueens N, followed by a new line,
            and exit with the status 1

        where N must be an integer greater or equal to 4

            If N is not an integer, print N must be a number,
            followed by a new line, and exit with the status 1
            If N is smaller than 4, print N must be at least 4,
            followed by a new line, and exit with the status 1

        The program should print every possible solution to the problem

            One solution per line
            Format: see example
            You don’t have to print the solutions in a specific order
    """
    print([[i, solution[i]] for i in range(len(solution))])


def is_safe(queen, row, col):
    for r in range(row):
        if queen[r] == col or \
           queen[r] - r == col - row or \
           queen[r] + r == col + row:
            return False
    return True


def solve_nqueens(N, row, queens, solutions):
    if row == N:
        solutions.append(queens[:])
        N_queens(queens)
        return
    for col in range(N):
        if is_safe(queens, row, col):
            queens[row] = col
            solve_nqueens(N, row + 1, queens, solutions)
            queens[row] = -1  # backtrack


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    queens = [-1] * N
    solve_nqueens(N, 0, queens, solutions)


if __name__ == "__main__":
    main()
