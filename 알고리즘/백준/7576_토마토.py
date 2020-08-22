import sys, collections
sys.stdin = open("7576_토마토.txt")


def bfs():
    global tomato, result
    while tomato:
        x, y = tomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0 and visited[nx][ny] == 0:
                    tomato.append([nx, ny])
                    box[nx][ny] = 1
                    visited[nx][ny] = visited[x][y] + 1
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                result = -1
                return
    maximum = 0
    for i in range(N):
        for j in range(M):
            if maximum < visited[i][j]:
                maximum = visited[i][j]
    print(maximum-1)


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 1
check_n = 0
tomato = collections.deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append([i, j])
            visited[i][j] = 1
        elif box[i][j] == -1:
            check_n += 1
if len(tomato) > 0 and len(tomato) + check_n == N*M:
    result = 0
elif len(tomato) == 0:
    result = -1
else:
    bfs()

if result != 1:
    print(result)

