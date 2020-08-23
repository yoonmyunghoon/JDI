import sys, collections
sys.stdin = open("2583_영역 구하기.txt")


def bfs(a, b):
    visited[a][b] = num
    n = 1
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
                    visited[nx][ny] = num
                    n += 1
    cnt.append(n)


N, M, K = map(int, input().split())
G = [[1 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
num = 0
cnt = []
for i in range(K):
    ax, ay, bx, by = map(int, input().split())
    for x in range(ax, bx):
        for y in range(ay, by):
            G[y][x] = 0
for i in range(N):
    for j in range(M):
        if G[i][j] == 1 and visited[i][j] == 0:
            num += 1
            bfs(i, j)
print(num)
cnt.sort()
for i in cnt:
    print(i, end=' ')