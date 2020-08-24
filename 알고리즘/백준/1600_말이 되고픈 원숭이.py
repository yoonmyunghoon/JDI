import sys, collections
sys.stdin = open("1600_말이 되고픈 원숭이.txt")


def bfs(a, b, k):
    visited[a][b][k] = 1
    deq = collections.deque()
    deq.append([a, b, k])
    while deq:
        x, y, k = deq.popleft()
        if x == H-1 and y == W-1 and k <= K:
            return visited[x][y][k] - 1
        if k < K:
            for i in range(12):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if i < 4:
                        if G[nx][ny] == 0 and visited[nx][ny][k] == 0:
                            deq.append([nx, ny, k])
                            visited[nx][ny][k] = visited[x][y][k] + 1
                    else:
                        if G[nx][ny] == 0 and visited[nx][ny][k+1] == 0:
                            deq.append([nx, ny, k + 1])
                            visited[nx][ny][k+1] = visited[x][y][k] + 1
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if G[nx][ny] == 0 and visited[nx][ny][k] == 0:
                        deq.append([nx, ny, k])
                        visited[nx][ny][k] = visited[x][y][k] + 1
    return -1

K = int(input())
W, H = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
dx = [-1, 0, 1, 0, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [0, 1, 0, -1, 1, 2, 2, 1, -1, -2, -2, -1]
print(bfs(0, 0, 0))