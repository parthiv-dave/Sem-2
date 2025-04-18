def solve_8_queens():
    def is_safe(board, row, col):

        for i in range(row):
            if board[i] == col:
                return False
        
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i] == j:
                return False
        
        for i, j in zip(range(row-1, -1, -1), range(col+1, 8)):
            if board[i] == j:
                return False
        
        return True

    def backtrack(board, row):
        if row == 8:
            solutions.append(board.copy())
            return
        
        for col in range(8):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * 8
    backtrack(board, 0)
    return solutions

all_solutions = solve_8_queens()

if all_solutions:
    first_solution = all_solutions[0]
    print("One possible solution:")
    for row in range(8):
        line = ['Q' if col == first_solution[row] else '.' for col in range(8)]
        print(' '.join(line))
else:
    print("No solutions found.")