"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid move")

    current_player = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if all(board[i][j] == X for j in range(3)) or all(board[j][i] == X for j in range(3)):
            return X
        elif all(board[i][j] == O for j in range(3)) or all(board[j][i] == O for j in range(3)):
            return O

    # Check diagonals
    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        return O

    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    return winner(board) is not None or all(board[i][j] != EMPTY for i in range(3) for j in range(3))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)

    return action


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float("-inf")
    best_action = None

    for action in actions(board):
        new_value, _ = min_value(result(board, action))
        if new_value > v:
            v = new_value
            best_action = action

    return v, best_action


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float("inf")
    best_action = None

    for action in actions(board):
        new_value, _ = max_value(result(board, action))
        if new_value < v:
            v = new_value
            best_action = action

    return v, best_action
