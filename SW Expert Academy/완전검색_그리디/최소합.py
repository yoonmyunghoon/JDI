import sys
sys.stdin = open("최소합.txt")

def iswall(x, y):
    if x < 0 or x >= N: return True
    elif y < 0 or y >= N: return True
    else: return False

def bfs(x, y):
    visited[x][y] = data[x][y]
    Q.append((x, y))
    while Q:
        a, b = Q.pop(0)
        for i in range(2):
            nx = a+dx[i]
            ny = b+dy[i]
            if iswall(nx, ny) == False:
                if visited[nx][ny] > visited[a][b] + data[nx][ny]:
                    visited[nx][ny] = visited[a][b] + data[nx][ny]
                    Q.append((nx, ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[10*N*N for _ in range(N)] for _ in range(N)]
    Q = []
    dx = [0, 1]
    dy = [1, 0]
    bfs(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))