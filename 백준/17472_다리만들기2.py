import sys, collections
sys.stdin = open('17472_다리만들기2.txt')

def find_set(x):
    if x == PI[x]: return x
    else: return find_set(PI[x])

def union(x, y):
    PI[find_set(y)] = find_set(x)

def mst():
    global cnt, result, total
    k = 0
    N = 0
    while N < cnt-1:
        if len(G_E) <= k:
            result = -1
            break
        if find_set(G_E[k][0]) != find_set(G_E[k][1]):
            union(G_E[k][0], G_E[k][1])
            total += G_E[k][2]
            N += 1
        k += 1

def bfs(x, y):
    global cnt
    visited[x][y] = cnt
    deq = collections.deque()
    deq.append((x, y))
    while deq:
        tx, ty = deq.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and G[nx][ny] == 1:
                visited[nx][ny] = cnt
                deq.append((nx, ny))

def connection(position):
    global NEWG, visited
    x = position[0]
    y = position[1]
    for i in range(4):
        tx = x
        ty = y
        count = 0
        while 1:
            tx += dx[i]
            ty += dy[i]
            if tx < 0 or tx >= N: break
            if ty < 0 or ty >= M: break
            if visited[tx][ty] != 0:
                if visited[tx][ty] == visited[x][y]: break
                if count >= 2:
                    if NEWG[visited[x][y]][visited[tx][ty]] > count:
                        NEWG[visited[x][y]][visited[tx][ty]] = count
                break
            count += 1

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for i in range(N):
    for j in range(M):
        if G[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            bfs(i, j)

NEWG = [[987654321 for _ in range(cnt+1)] for _ in range(cnt+1)]
for i in range(N):
    for j in range(M):
        if visited[i][j] != 0:
            connection((i, j))
G_E = []
PI = list(range(cnt+1))
for i in range(len(NEWG)):
    for j in range(i + 1, len((NEWG))):
        if NEWG[i][j] != 987654321:
            G_E.append([i, j, NEWG[i][j]])
G_E.sort(key=lambda x:x[2])
print(cnt)
print(G_E)
result = 0
total = 0
mst()
if result == -1:
    print(-1)
else:
    print(total)

