import sys, collections
sys.stdin = open("14442_벽 부수고 이동하기2.txt")


def bfs(a, b, c):
    visited[a][b][c] = 1
    deq = collections.deque()
    deq.append([a, b, c])
    while deq:
        x, y, k = deq.popleft()
        if x == N-1 and y == M-1:
            result.append(visited[x][y][k])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if k < K:
                    if G[nx][ny] == 0 and visited[nx][ny][k] == 0:
                        deq.append([nx, ny, k])
                        visited[nx][ny][k] = visited[x][y][k] + 1
                    elif G[nx][ny] == 1 and visited[nx][ny][k+1] == 0:
                        deq.append([nx, ny, k+1])
                        visited[nx][ny][k+1] = visited[x][y][k] + 1
                else:
                    if G[nx][ny] == 0 and visited[nx][ny][k] == 0:
                        deq.append([nx, ny, k])
                        visited[nx][ny][k] = visited[x][y][k] + 1


N, M, K = map(int, input().split())
G = [list(map(int, input())) for _ in range(N)]
visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = []
bfs(0, 0, 0)
if result:
    print(min(result))
else:
    print(-1)