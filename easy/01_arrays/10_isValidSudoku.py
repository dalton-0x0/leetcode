"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
def isValidSudoku(board):
    # Check rows
    for row in board:
        if not isValidGroup(row):
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not isValidGroup(column):
            return False

    # Check 3x3 sub-boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not isValidGroup(sub_box):
                return False

    return True

def isValidGroup(group):
    seen = set()
    for cell in group:
        if cell != '.':
            if cell in seen:
                return False
            seen.add(cell)
    return True


# Example board to test
test_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Alternate solution
def isValidSudoku_2(board):
    # Initialize sets to track seen numbers in rows, columns, and sub-boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Traverse the board
    for r in range(9):
        for c in range(9):
            num = board[r][c]

            # Skip empty cells
            if num == '.':
                continue

            # Check row
            if num in rows[r]:
                return False
            rows[r].add(num)
            # print(rows)

            # Check column
            if num in cols[c]:
                return False
            cols[c].add(num)
            # print(cols)

            # Check sub-box
            box_index = (r // 3) * 3 + (c // 3)
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)

    # If no violations, the board is valid
    print("row sets:", rows)
    print("col sets:", cols)
    return True

print("Solution 1:")
print(isValidSudoku(test_board)) # True
print("Solution 2:")
print(isValidSudoku_2(test_board)) # True
