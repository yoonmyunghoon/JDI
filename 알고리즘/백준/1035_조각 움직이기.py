import sys
sys.stdin = open("1035_조각 움직이기.txt")


def find(n):
    global p
    if p[n] < 0:
        return n
    else:
        return find(p[n])


def union(a, b):
    global p
    a = find(a)
    b = find(b)
    if a == b:
        return
    else:
        p[b] = a


def move(k, cnt):
    global minimum
    if minimum <= cnt:
        return
    if check() == 1:
        if minimum > cnt:
            minimum = cnt
        return
    for i in range(4):
        bx = position[k][0]
        by = position[k][1]
        nx = bx + dx[i]
        ny = by + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if board[nx][ny] == '.' and visited[k][nx][ny] == 0:
                board[nx][ny] = '*'
                board[bx][by] = '.'
                position[k] = [nx, ny]
                visited[k][nx][ny] = 1
                for j in range(N):
                    visited[j][position[j][0]][position[j][1]] = 1
                    move(j, cnt+1)
                    visited[j][position[j][0]][position[j][1]] = 0
                board[nx][ny] = '.'
                board[bx][by] = '*'
                position[k] = [bx, by]
                visited[k][nx][ny] = 0


def check():
    global p
    p = [-1]*N
    for i in range(N-1):
        for j in range(i+1, N):
            if diff(position[i][0], position[j][0]) + diff(position[i][1], position[j][1]) == 1:
                union(i, j)
    if p.count(-1) == 1 and p.count(p[p.index(-1)-1]) == N-1:
        return 1
    else:
        return 0


def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a


board = [list(input()) for _ in range(5)]
visited0 = [[0 for _ in range(5)] for _ in range(5)]
visited1 = [[0 for _ in range(5)] for _ in range(5)]
visited2 = [[0 for _ in range(5)] for _ in range(5)]
visited3 = [[0 for _ in range(5)] for _ in range(5)]
visited4 = [[0 for _ in range(5)] for _ in range(5)]
visited = [visited0, visited1, visited2, visited3, visited4]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
position = []
for i in range(5):
    for j in range(5):
        if board[i][j] == '*':
            position.append([i, j])
N = len(position)
print(N)
print(position)
p = [-1]*N
minimum = 987654321
for i in range(N):
    visited[i][position[i][0]][position[i][1]] = 1
    move(i, 1)
    visited[i][position[i][0]][position[i][1]] = 0
print(minimum)



