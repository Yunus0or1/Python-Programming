from copy import deepcopy

result = []
N = 0

def createBoard(n):
    board = []
    for x in range(n):
        row = []
        for y in range(n):
            row.append(0)

        board.append(row)

    return board


def isSafe(board, row, column):
    # We do not need to check any bottom rows because
    # There is nothing yet

    # Above Straight Rows
    for i in range(0, row):
        if board[i][column] == 1:
            return False

    # Left Upper diagonal check
    i = row
    j = column
    while i > -1 and j > -1:
        if board[i][j] == 1:
            return False

        i = i - 1
        j = j - 1

    # Right upper diagonal check
    i = row
    j = column
    while i > -1 and j < len(board):
        if board[i][j] == 1:
            return False

        i = i - 1
        j = j + 1

    return True


def solveNQueenUtil(board, row):
    if row >= N:
        result.append(deepcopy(board))
        return

    for column in range(0, N):
        if isSafe(board, row, column):
            board[row][column] = 1
            solveNQueenUtil(board, row + 1)
            board[row][column] = 0

def initial():
    board = createBoard(N)
    solveNQueenUtil(board, 0)

initial()
print(result)
