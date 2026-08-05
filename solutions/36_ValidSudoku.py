def isValidSudoku(board):
    def isValidEntry(entry):
        seen = set()

        for val in entry:
            if val == '.':
                continue

            if val in seen:
                return False

            seen.add(val)
        return True

    for row in board:
        if not isValidEntry(row):
            return False

    for i in range(len(board)):
        col = []

        for j in range(len(board[i])):
           col.append(board[j][i])
        
        if not isValidEntry(col):
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            box = []

            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    box.append(board[r][c])

            if not isValidEntry(box):
                return False
    return True


def isValidSudoku_old(board):
    def isValidEntry(entry):
        seen = []

        for val in entry:
            # print(ent)
            if val in seen:
                return False
            if val != '.':
                seen.append(val)
        return True

    for row in board:
        # print(row, isValidEntry(row))
        if not isValidEntry(row):
            return False
    # print("col,row")

    for i in range(len(board)):
        col = []

        for j in range(len(board[i])):
           col.append(board[j][i])
        
        if not isValidEntry(col):
            return False
    pivots = [[1,1], [1,4], [1, 7],
              [4,1], [4,4], [4,7],
              [7,1], [7,4], [7,7]]

    for pivot in pivots:
        box = [
            board[pivot[0] - 1][pivot[1] - 1], board[pivot[0] - 1][pivot[1]], board[pivot[0] - 1][pivot[1] + 1],
            board[pivot[0]][pivot[1] - 1], board[pivot[0]][pivot[1]], board[pivot[0]][pivot[1] + 1],
            board[pivot[0] + 1][pivot[1] - 1], board[pivot[0] + 1][pivot[1]], board[pivot[0] + 1][pivot[1] + 1],
        ]
        # print(box)
        if not isValidEntry(box):
            return False
    return True

print(isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))

print(isValidSudoku(
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))

