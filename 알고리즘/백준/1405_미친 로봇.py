import sys
sys.stdin = open("1405_미친 로봇.txt")


def move(n, p, x, y):
    global result
    if n == N:
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if visited[nx][ny]:
            result += p*D[i]
            continue
        else:
            visited[nx][ny] = 1
            move(n+1, p*D[i], nx, ny)
            visited[nx][ny] = 0


data = list(map(int, input().split()))
N = data[0]
D = data[1:]
D = list(map(lambda x: x/100, D))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0 for _ in range(N*2+1)] for _ in range(N*2+1)]
visited[N][N] = 1
result = 0
move(0, 1, N, N)
print(1-result)