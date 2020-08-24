import sys, collections
sys.stdin = open("6087_레이저 통신.txt")


def bfs(a, b, k):
    global result
    for i in range(4):
        visited[a][b][i] = 1
    deq = collections.deque()
    deq.append([a, b, k])
    while deq:
        x, y, d = deq.popleft()
        if x == C_position[1][0] and y == C_position[1][1]:
            result.append(visited[x][y][d]-1)
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < H and 0 <= ny < W:
                if G[nx][ny] != '*':
                    if d == -1:
                        if visited[nx][ny][j] == 0:
                            deq.append([nx, ny, j])
                            visited[nx][ny][j] = 1
                    else:
                        if j == d:
                            if visited[nx][ny][j] > visited[x][y][j] or visited[nx][ny][j] == 0:
                                deq.append([nx, ny, j])
                                visited[nx][ny][j] = visited[x][y][j]
                        else:
                            if visited[nx][ny][j] > visited[x][y][d] + 1 or visited[nx][ny][j] == 0:
                                deq.append([nx, ny, j])
                                visited[nx][ny][j] = visited[x][y][d] + 1


W, H = map(int, input().split())
G = [list(input()) for _ in range(H)]
visited = [[[0 for _ in range(4)] for _ in range(W)] for _ in range(H)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
C_position = []
result = []
for i in range(H):
    for j in range(W):
        if G[i][j] == 'C':
            C_position.append([i, j])
bfs(C_position[0][0], C_position[0][1], -1)
print(min(result))