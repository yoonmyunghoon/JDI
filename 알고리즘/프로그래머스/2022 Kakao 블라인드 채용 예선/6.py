# def solution(board, skill):
#     N = len(board)
#     M = len(board[0])
#     answer = 0
#     skill.sort()
#     for skill_info in skill:
#         skill_type, r1, c1, r2, c2, degree = skill_info
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 board[i][j] += degree*((-1)**skill_type)
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] > 0:
#                 answer += 1
#     return answer


def solution(board, skill):
    N = len(board)
    M = len(board[0])
    answer = 0
    damaged_dict = {}
    for skill_info in skill:
        skill_type, r1, c1, r2, c2, degree = skill_info
        if (r1, c1, r2, c2) in damaged_dict:
            damaged_dict[(r1, c1, r2, c2)] += degree*((-1)**skill_type)
        else:
            damaged_dict[(r1, c1, r2, c2)] = degree*((-1)**skill_type)
    for k, v in damaged_dict.items():
        for i in range(k[0], k[2]+1):
            for j in range(k[1], k[3]+1):
                board[i][j] += v
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                answer += 1
    return answer


board_ex = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill_ex = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board_ex, skill_ex))