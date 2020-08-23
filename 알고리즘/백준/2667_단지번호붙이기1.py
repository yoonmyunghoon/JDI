import sys, collections
sys.stdin = open("2667_단지번호붙이기.txt")


def dfs(x, y):
    visited[x][y] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and G[nx][ny] != 0:
            dfs(nx, ny)

N = int(input())
G = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for i in range(N):
    for j in range(N):
        if G[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            dfs(i, j)
counts = []
for i in range(1, cnt+1):
    count = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y] == i:
                count += 1
    counts.append(count)

print(cnt)
counts.sort()
for i in counts:
    print(i)