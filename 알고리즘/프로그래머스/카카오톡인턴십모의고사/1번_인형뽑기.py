
def solution(board, moves):
    barguni = []
    cnt = 0
    for p in moves:
        n = 0
        empty = 0
        inhyung = 0
        while 1:
            if n >= len(board):
                empty = 1
                break
            if board[n][p-1] != 0:
                inhyung = board[n][p-1]
                board[n][p-1] = 0
                break
            n += 1
        if empty == 0:
            if len(barguni) == 0:
                barguni.append(inhyung)
            else:
                if barguni[-1] == inhyung:
                    barguni.pop()
                    cnt += 2
                else:
                    barguni.append(inhyung)
    return cnt

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))