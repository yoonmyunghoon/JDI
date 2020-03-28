import sys, collections
sys.stdin = open("BJ_2589_보물섬.txt")

def bfs(x, y):
    global visited, distance
    visited[x][y] = 1
    deq = collections.deque()
    deq.append([x, y])
    while deq:
        tx, ty = deq.popleft()
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and map[nx][ny] == 'L':
                visited[nx][ny] = visited[tx][ty] + 1
                if distance < visited[nx][ny] - 1:
                    distance = visited[nx][ny] - 1
                deq.append([nx, ny])

N, M = map(int, input().split())
map = [list(map(str, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
distance = 0
for i in range(N):
    for j in range(M):
        if map[i][j] == 'L':
            visited = [[0 for _ in range(M)] for _ in range(N)]
            bfs(i, j)
print(distance)
