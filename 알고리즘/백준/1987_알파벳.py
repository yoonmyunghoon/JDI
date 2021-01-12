import sys
sys.stdin = open("1987_알파벳.txt")


def dfs(x, y, d):
    global max_d
    if max_d < d:
        max_d = d
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if passed[Map[nx][ny]] == 0:
                passed[Map[nx][ny]] = 1
                dfs(nx, ny, d+1)
                passed[Map[nx][ny]] = 0


# R, C = map(int, input().split())
# Map = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]
R, C = map(int, sys.stdin.readline().split())
Map = [list(map(lambda x: ord(x)-65, sys.stdin.readline().strip())) for _ in range(R)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
passed = [0]*26
max_d = 0
passed[Map[0][0]] = 1
dfs(0, 0, 1)
print(max_d)