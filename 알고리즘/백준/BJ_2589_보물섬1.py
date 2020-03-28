import sys, collections
sys.stdin = open("BJ_2589_보물섬1.txt")

def i_find(x, y):
    global visited1, n
    visited1[x][y] = n
    deq = collections.deque()
    deq.append([x, y])
    while deq:
        tx, ty = deq.popleft()
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited1[nx][ny] == 0 and map[nx][ny] == 'L':
                visited1[nx][ny] = n
                deq.append([nx, ny])

def bfs(x, y):
    global visited
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
                deq.append([nx, ny])

N, M = map(int, input().split())
map = [list(map(str, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited1 = [[0 for _ in range(M)] for _ in range(N)]
checked = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = 0
i_counts = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 'L' and visited1[i][j] == 0:
            n += 1
            i_find(i, j)
for q in range(1, n+1):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited1[i][j] == q:
                cnt += 1
    i_counts.append(cnt)
# print(i_counts)
# print(n)
distance = 0
for q in range(n):
    if i_counts[q]-1 > distance:
        for i in range(N):
            for j in range(M):
                if map[i][j] == 'L' and checked[i][j] == 0 and visited1[i][j] == q+1:
                    checked[i][j] = 1
                    visited = [[0 for _ in range(M)] for _ in range(N)]
                    bfs(i, j)
                    md = max(sum(visited, []))
                    if distance < md-1:
                        distance = md-1
print(distance)
