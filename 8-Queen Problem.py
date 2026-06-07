N = 8

def solve(board, row):
    if row == N:
        for r in board:
            print(r)
        return True

    for col in range(N):
        safe = True
        for i in range(row):
            q = board[i].index('Q')
            if q == col or abs(q-col) == abs(i-row):
                safe = False

        if safe:
            board[row][col] = 'Q'
            if solve(board, row+1):
                return True
            board[row][col] = '.'

board = [['.']*N for _ in range(N)]
solve(board,0)
