import sys, collections
sys.stdin = open("5022_연결.txt")


def bfs(a, b, c):
    visited[a][b] = 1
    deq = collections.deque()
    check = []
    deq.append([a, b, 1, 0])
    number = 1
    while deq:
        x, y, num, parent = deq.popleft()
        check.append([x, y, num, parent])
        if c == 2:
            if x == A2[0] and y == A2[1]:
                p = check[-1][3]
                while 1:
                    if p == 0:
                        break
                    for g in range(len(check)):
                        if check[g][2] == p:
                            G[check[g][0]][check[g][1]] = 1
                            p = check[g][3]
                return visited[x][y] - 1
        if c == 1:
            if x == B2[0] and y == B2[1]:
                p = check[-1][3]
                while 1:
                    if p == 0:
                        break
                    for g in range(len(check)):
                        if check[g][2] == p:
                            G[check[g][0]][check[g][1]] = 2
                            p = check[g][3]
                return visited[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N+1 and 0 <= ny < M+1:
                if G[nx][ny] != c and visited[nx][ny] == 0:
                    number += 1
                    deq.append([nx, ny, number, num])
                    visited[nx][ny] = visited[x][y] + 1
    return -1


N, M = map(int, input().split())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
B1 = list(map(int, input().split()))
B2 = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

G = [[0 for _ in range(M+1)] for _ in range(N+1)]
visited = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(M+1):
        if [i, j] == A1 or [i, j] == A2:
            G[i][j] = 1
        if [i, j] == B1 or [i, j] == B2:
            G[i][j] = 2

result1 = 0
result2 = 0

a = bfs(A1[0], A1[1], 2)
visited = [[0 for _ in range(M+1)] for _ in range(N+1)]
b = bfs(B1[0], B1[1], 1)
if b == -1:
    result1 = -1
else:
    result1 = a + b

G = [[0 for _ in range(M+1)] for _ in range(N+1)]
visited = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(M+1):
        if [i, j] == A1 or [i, j] == A2:
            G[i][j] = 1
        if [i, j] == B1 or [i, j] == B2:
            G[i][j] = 2

c = bfs(B1[0], B1[1], 1)
visited = [[0 for _ in range(M+1)] for _ in range(N+1)]
d = bfs(A1[0], A1[1], 2)
if d == -1:
    result2 = -1
else:
    result2 = c + d

if result1 == -1 and result2 == -1:
    print('IMPOSSIBLE')
elif result2 == -1:
    print(result1)
elif result1 == -1:
    print(result2)
else:
    print(min(result1, result2))


