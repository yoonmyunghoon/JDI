import sys, collections
sys.stdin = open('16236_아기상어.txt')

def bfs(x, y):
    global size, time, cnt, position, visited
    visited[x][y] = 1
    deq = collections.deque()
    deq.append((x, y))
    while deq:
        tx, ty = deq.popleft()
        if G[tx][ty] < size:
            G[tx][ty] = 0
            time += visited[tx][ty]
            position = [tx, ty]
            cnt += 1
            if cnt == size:
                size += 1
            return
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < N and G[nx][ny] <= size:
                visited[nx][ny] = visited[tx][ty] + 1
                deq.append((nx, ny))

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

position = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 9:
            position = [i, j]
size = 2
cnt = 0
time = 0

while 1:
    num0 = 0
    numsmall = 0
    for i in range(N):
        for j in range(N):
            if G[i][j] == 0:
                num0 += 1
            elif G[i][j] < size:
                numsmall += 1
    if num0 == N*N-1 or numsmall == 0:
        break
    else:
        bfs(position[0], position[1])
        visited = [[0 for _ in range(N)] for _ in range(N)]
print(time)