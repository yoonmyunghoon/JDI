def solution(board, moves):

    def check_stack(p):
        if len(stack) == 0:
            stack.append(p)
            return 0
        else:
            if stack[-1] == p:
                stack.pop()
                return 2
            else:
                stack.append(p)
                return 0
    answer = 0
    stack = []
    size = len(board)
    for move in moves:
        position = move - 1
        h = 0
        while 1:
            if h == size:
                break
            if board[h][position] != 0:
                answer += check_stack(board[h][position])
                board[h][position] = 0
                break
            h += 1
    return answer


board_ex = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves_ex = [1,5,3,5,1,2,1,4]
print(solution(board_ex, moves_ex))