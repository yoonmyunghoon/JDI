import sys
sys.stdin = open("14503_로봇청소기.txt")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# 0: 북(위), 1: 동(오른쪽), 2: 남(아래), 3: 서(왼쪽)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = r, c
cnt = 0
while 1:
    visited[x][y] = 1
    nx = x + dx[(d + 3) % 4]
    ny = y + dy[(d + 3) % 4]
    if visited[nx][ny] == 0 and G[nx][ny] == 0:
        d = (d + 3) % 4
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt = 0
    else:
        d = (d + 3) % 4
        cnt += 1
    if cnt == 4:
        tx = x + dx[(d + 2) % 4]
        ty = y + dy[(d + 2) % 4]
        if G[tx][ty] == 0:
            x = tx
            y = ty
            cnt = 0
        else:
            break
result = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            result += 1

print(result)