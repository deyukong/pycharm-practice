board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    , [4, 9, 8, 2, 6, 1, 3, 7, 5]
    , [7, 5, 6, 3, 8, 4, 2, 1, 9]
    , [6, 4, 3, 1, 5, 8, 7, 9, 2]
    , [5, 2, 1, 7, 9, 3, 8, 4, 6]
    , [9, 8, 7, 4, 2, 6, 5, 3, 1]
    , [2, 1, 4, 9, 3, 5, 6, 8, 7]
    , [3, 6, 5, 8, 1, 7, 9, 2, 4]
    , [8, 7, 9, 6, 4, 2, 1, 5, 3]]

bboard = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    , [4, 9, 8, 2, 6, 1, 3, 7, 5]
    , [7, 5, 6, 3, 8, 4, 2, 1, 9]
    , [6, 4, 3, 1, 5, 8, 7, 9, 2]
    , [5, 2, 1, 7, 9, 3, 8, 4, 6]
    , [9, 8, 7, 4, 2, 6, 5, 3, 1]
    , [2, 1, 4, 9, 3, 5, 6, 8, 7]
    , [3, 6, 5, 8, 1, 7, 9, 2, 4]
    , [8, 7, 9, 6, 4, 2, 1, 3, 5]]


def done_or_not(board):  # board[i][j]

    if len(board) == 0:
        return ('Try again!')

    for i in range(0, 9):
        # print(len(set(board[i])))
        if len(set(board[i])) != 9:
            return ('Try again!')

        # check every column
        col = []
        for j in range(0, 9):
            col.append(board[j][i])
        # print(len(set(col)))
        if len(set(col)) != 9:
            return ('Try again!')

        x = (i // 3) * 3
        y = (i % 3) * 3
        reg = []

        for a in range(0, 3):
            for b in range(0, 3):
                reg.append(board[x + a][y + b])
        if len(set(reg)) != 9:
            return ('Try again!')

    return ('Finished!')