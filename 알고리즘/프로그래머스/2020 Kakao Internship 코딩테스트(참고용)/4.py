# 방향 바꿀때 500원 아니면 100원씩 증가 힙 사용 다익스트라
import heapq

inf = 0xfffffff
D = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def solution(board):
    # 방향 바꿀때 500원 아니면 100원씩 증가 힙 사용 다익스트라
    nl = [[[0 if board[j][i] else inf for k in range(4)] for i in range(len(board))] for j in range(len(board))]
    result = inf
    for dir in range(4):
        Q = [[0, dir, 0, 0]]
        while Q:
            money, cdir, x, y = heapq.heappop(Q)
            if money > nl[y][x][cdir]:
                continue
            if x == len(board)-1 and y == len(board)-1:
                result = min(result, money)
                break
            for i in range(len(D)):
                tx = x + D[i][0]
                ty = y + D[i][1]
                if 0 <= tx < len(board) and 0 <= ty < len(board) and not board[ty][tx]:
                    tmoney = money + 100
                    if i != cdir:
                        tmoney += 500
                    if nl[ty][tx][i] > tmoney:
                        nl[ty][tx][i] = tmoney
                    if tmoney < result:
                        heapq.heappush(Q, [tmoney, i, tx, ty])

    answer = result
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))