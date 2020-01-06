import sys
sys.stdin = open("BJ_17070_파이프 옮기기1.txt")

# d: 파이프 방향
def dfs(x, y, d):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
    if d == 0:
        if 0 <= x+1 < N and 0 <= y+1 < N:
            if house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
                dfs(x + 1, y + 1, 2)
        if 0 <= y+1 < N:
            if house[x][y+1] == 0:
                dfs(x, y + 1, 0)
    elif d == 1:
        if 0 <= x + 1 < N and 0 <= y + 1 < N:
            if house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
                dfs(x + 1, y + 1, 2)
        if 0 <= x + 1 < N:
            if house[x+1][y] == 0:
                dfs(x + 1, y, 1)
    else:
        if 0 <= x + 1 < N and 0 <= y + 1 < N:
            if house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
                dfs(x + 1, y + 1, 2)
        if 0 <= y + 1 < N:
            if house[x][y+1] == 0:
                dfs(x, y + 1, 0)
        if 0 <= x + 1 < N:
            if house[x+1][y] == 0:
                dfs(x + 1, y, 1)

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 0)
print(cnt)