import sys
sys.stdin = open("1937_욕심쟁이 판다.txt")

def dfs(x, y, d):
    check[x][y] = d
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
            dfs(nx, ny, d + 1)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    for j in range(n):
        dfs(i, j, 1)
        print([i, j])
        for k in check:
            print(k)
        print()

maximun = 0
for i in check:
    if maximun < max(i):
        maximun = max(i)
print(maximun)