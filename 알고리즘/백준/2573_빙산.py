import sys, collections
sys.stdin = open("2573_빙산.txt")


def bfs(a, b):
    visited[a][b] = 1
    deq = collections.deque()
    deq.append([a, b])
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if G[nx][ny] != 0 and visited[nx][ny] == 0:
                    deq.append([nx, ny])
                    visited[nx][ny] = 1


def counting():
    global visited
    visited = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] != 0 and visited[i][j] == 0:
                count += 1
                bfs(i, j)
    return count


def melting_ice():
    for i in range(N):
        for j in range(M):
            if G[i][j] != 0:
                c = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < N and 0 <= y < M:
                        if G[x][y] == 0:
                            c += 1
                melted[i][j] = c
    for i in range(N):
        for j in range(M):
            if melted[i][j] != 0:
                if G[i][j] - melted[i][j] < 0:
                    G[i][j] = 0
                else:
                    G[i][j] = G[i][j] - melted[i][j]
                melted[i][j] = 0


def check():
    for i in range(N):
        for j in range(M):
            if G[i][j] != 0:
                return 1
    return 0


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
melted = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
time = 0
cnt = 1
while 1:
    if cnt >= 2:
        print(time)
        break
    if check() == 0:
        print(0)
        break
    melting_ice()
    time += 1
    cnt = counting()



