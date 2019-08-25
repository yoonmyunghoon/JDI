import sys
sys.stdin = open("input.txt")

def isWall(x, y):
    if x < 0 or x > N-1: return True
    elif y < 0 or y > N-1: return True
    elif G[x][y] == 0: return True
    else: return False

def dfs(x, y):
    global count, cnt
    visitied[x][y] = count
    cnt += 1
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if isWall(newX, newY) == False and visitied[newX][newY] == 0:
            dfs(newX, newY)

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
visitied = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
counts = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 1 and visitied[i][j] == 0:
            count += 1
            cnt = 0
            dfs(i,j)
            counts.append(cnt)
print(count)
print(counts)
for i in G:
    print(i)
print()
for i in visitied:
    print(i)
