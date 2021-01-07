import sys
sys.stdin = open("1189_컴백홈.txt")


def dfs(x, y, d):
    global cnt
    visited[x][y] = d
    if d > K:
        return
    if x == 0 and y == C-1 and d == K:
        cnt += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if visited[nx][ny] == 0 and Map[nx][ny] == '.':
                dfs(nx, ny, d+1)
                visited[nx][ny] = 0


R, C, K = map(int, input().split())
Map = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cnt = 0
dfs(R-1, 0, 1)
print(cnt)


