import sys, collections
sys.stdin = open("2178_미로 탐색.txt")


def bfs(a, b):
    visited[a][b] = 1
    deq = collections.deque()
    deq.append((a, b))
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if map[nx][ny] == 1 and visited[nx][ny] == 0:
                    deq.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


N, M = map(int, input().split())
map = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
bfs(0, 0)

print(visited[N-1][M-1])