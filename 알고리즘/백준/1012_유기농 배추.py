import sys, collections
sys.stdin = open("1012_유기농 배추.txt")


def bfs(a, b):
    visited[a][b] = 1
    deq = collections.deque()
    deq.append([a, b])
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if G[nx][ny] == 1 and visited[nx][ny] == 0:
                    deq.append([nx, ny])
                    visited[nx][ny] = 1


T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for tc in range(T):
    M, N, K = map(int, input().split())
    G = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for i in range(K):
        x, y = map(int, input().split())
        G[y][x] = 1
    for i in range(N):
        for j in range(M):
            if G[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)
    print(cnt)