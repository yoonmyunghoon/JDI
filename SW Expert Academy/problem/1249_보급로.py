import sys
sys.stdin = open("1249_보급로.txt")

def isWall(x, y):
    if x < 0 or x >= N: return True
    elif y < 0 or y >= N: return True
    else: return False

def bfs(v, w):
    global N
    visited[v][w] = 0
    Q.append((v, w))
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if isWall(newX, newY) == False:
                if visited[newX][newY] > visited[x][y] + G[newX][newY]:
                    visited[newX][newY] = visited[x][y] + G[newX][newY]
                    Q.append((newX, newY))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [list(map(int, input())) for _ in range(N)]
    visited = [[N*N*9 for _ in range(N)] for _ in range(N)]
    Q = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    bfs(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))