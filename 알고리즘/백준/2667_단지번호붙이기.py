import sys, collections
sys.stdin = open("2667_단지번호붙이기.txt")


def bfs(a, b):
    visited[a][b] = num
    deq = collections.deque()
    deq.append([a, b])
    n = 1
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if G[nx][ny] == 1 and visited[nx][ny] == 0:
                    deq.append([nx, ny])
                    visited[nx][ny] = num
                    n += 1
    cnt.append(n)


N = int(input())
G = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
num = 0
cnt = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(N):
        if G[i][j] == 1 and visited[i][j] == 0:
            num += 1
            bfs(i, j)

print(num)
cnt.sort()
for i in cnt:
    print(i)
