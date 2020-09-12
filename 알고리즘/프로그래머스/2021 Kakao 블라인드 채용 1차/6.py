from itertools import permutations
from collections import deque
from copy import deepcopy


def solution(board_o, r, c):
    board = deepcopy(board_o)

    def bfs(t, n, a, b):
        visited = [[0] * 4 for _ in range(4)]
        visited[a][b] = 1
        deq = deque()
        deq.append([a, b])
        while deq:
            x, y = deq.popleft()
            for i in range(8):
                if 0 <= i < 4:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1
                            deq.append([nx, ny])
                else:
                    nx = x
                    ny = y
                    while 1:
                        nx = nx + dx[i % 4]
                        ny = ny + dy[i % 4]
                        if not (0 <= nx < 4 and 0 <= ny < 4):
                            nx = nx - dx[i % 4]
                            ny = ny - dy[i % 4]
                            if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                                visited[nx][ny] = visited[x][y] + 1
                                deq.append([nx, ny])
                            break
                        if board[nx][ny] != 0 and (visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1):
                            visited[nx][ny] = visited[x][y] + 1
                            deq.append([nx, ny])
                            break
        info = []
        for i in range(4):
            for j in range(4):
                if board[i][j] == n:
                    info.append([visited[i][j], i, j])
        info.sort()
        return info[0][1], info[0][2], info[0][0]

    maximum = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for row in board:
        if maximum < max(row):
            maximum = max(row)
    card_num = list(range(1, maximum+1))
    order_list = list(permutations(card_num, maximum))
    minimum = []
    for od in order_list:
        tx = r
        ty = c
        ret = 0
        board = deepcopy(board_o)
        for d in od:
            tx, ty, cnt = bfs(0, d, tx, ty)
            ret += cnt
            board[tx][ty] = 0
            tx, ty, cnt = bfs(1, d, tx, ty)
            ret += cnt
            board[tx][ty] = 0
        minimum.append(ret)
    print(minimum)
    return min(minimum)


B = [[1,0,0,3],
     [2,0,0,0],
     [0,0,0,2],
     [3,0,1,0]]
R = 1
C = 0
print(solution(B, R, C))