import sys, collections
sys.stdin = open('16236_아기상어.txt')

def bfs(x, y):
    global size, time, cnt, position, visited, tmp
    visited[x][y] = 1
    deq = collections.deque()
    deq.append((x, y))
    checkposition = []
    checkscore = 987654321
    while deq:
        tx, ty = deq.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < N and G[nx][ny] <= size and visited[nx][ny] == 0 and visited[tx][ty] <= checkscore:
                if G[nx][ny] == 0 or G[nx][ny] == size:
                    visited[nx][ny] = visited[tx][ty] + 1
                    deq.append((nx, ny))
                else:
                    checkposition.append([visited[tx][ty], nx, ny])
                    checkscore = visited[tx][ty]
    if len(checkposition) > 0:
        G[position[0]][position[1]] = 0
        checkposition.sort()
        G[checkposition[0][1]][checkposition[0][2]] = 9
        time += checkposition[0][0]
        position = [checkposition[0][1], checkposition[0][2]]
        if size < 7:
            cnt += 1
            if cnt == size:
                size += 1
                cnt = 0
        return
    else:
        tmp = 1

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
tmp = 0
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
    if num0 == N*N-1 or numsmall == 0 or tmp == 1:
        break
    else:
        bfs(position[0], position[1])
        visited = [[0 for _ in range(N)] for _ in range(N)]
print(time)