'''Puzzle game'''
def validate_board(board:list) -> bool:
    '''
    Покликання на GitHub:
    https://github.com/shshrg/Shergina-Oleksandra-lab8-task2.git

    Checks if the board is ready to start the game.
    >>> board = ["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *",\
"3   1  **", "  8  2***", "  2  ****"]
    >>> validate_board(board)
    False
    '''
    for row in board:
        if len(row) != 9:
            return False
        for sym in row:
            if sym.isdigit() and row.count(sym) > 1:
                return False
        for k in range(9):
            numbers_dont_repeat = [row[k] != x[k] for x in board if row != x and row[k].isdigit()]
            if not all(numbers_dont_repeat):
                return False
    s1 = board[0][4]+board[1][4]+board[2][4]+board[3][4]+board[4][4:9]
    s2 = board[1][3]+board[2][3]+board[3][3]+board[4][3]+board[5][3:8]
    s3 = board[2][2]+board[3][2]+board[4][2]+board[5][2]+board[6][2:7]
    s4 = board[3][1]+board[4][1]+board[5][1]+board[6][1]+board[7][1:6]
    s5 = board[4][0]+board[5][0]+board[6][0]+board[7][0]+board[8][0:5]
    for segment in [s1, s2, s3, s4, s5]:
        print(segment)
        for x in segment:
            if segment.count(x) > 1:
                return False
    return True
