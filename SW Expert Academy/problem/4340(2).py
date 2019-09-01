import sys
sys.stdin = open("input.txt")

def isWall(x, y):
    if x < 0 or x >= N: return True
    elif y < 0 or y >= N: return True
    elif pipe[x][y] == 0: return True
    else: return False

def move(x, y, count):
    visited[x][y] = 1
    Q.append([x, y])
    while Q:
        t = Q.pop(0)
        for i in range(4):
            newX = t[0] + dx[i]
            newY = t[1] + dy[i]
            if isWall(newX, newY) == False and visited[newX][newY] == 0:
                if pipe[t[0]][t[1]] == 1 or pipe[t[0]][t[1]] == 3 or pipe[t[0]][t[1]] == 6:
                    if pipe[newX][newY] == 1 or pipe[newX][newY] == 2:
                        pipe[newX][newY] = 1
                        visited[newX][newY] = 1
                        Q.append([newX, newY])
                    else:
                        pipe[newX][newY] = 4
                        Q.append([newX, newY])
                        visited[newX][newY] = 1
                        pipe[newX][newY] = 5








T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pipe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    Q = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    data = []
    Min = N*N
    move(0, 0)
    print(data)
    print()
    for i in pipe:
        print(i)
    print()
    print()
    for i in visited:
        print(i)
    print()
    print()

