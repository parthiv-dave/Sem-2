import random

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def place_queens_randomly():
    board = [-1] * 8
    for row in range(8):
        columns = list(range(8))
        random.shuffle(columns)
        for col in columns:
            if is_safe(board, row, col):
                board[row] = col
                break
        else:
            return None
    return board

def find_solution():
    while True:
        solution = place_queens_randomly()
        if solution is not None:
            return solution

solution = find_solution()
print("Randomly generated solution:")
for row in range(8):
    line = ['Q' if col == solution[row] else '.' for col in range(8)]
    print(' '.join(line))