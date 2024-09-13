#!/usr/bin/python3

"""N-Queens problem using backtracking."""
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the current column and diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Backtracking solution to find all N-Queens solutions."""
    def backtrack(row, board):
        # Base case: If all queens are placed, add solution
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return

        # Try placing a queen in all columns of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1  # Backtrack

    solutions = []
    board = [-1] * N  # Initialize the board
    backtrack(0, board)
    return solutions


def main():
    """Main function to validate input and print solutions."""
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

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
