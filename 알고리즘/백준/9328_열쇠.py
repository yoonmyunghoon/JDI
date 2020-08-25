import sys, collections
sys.stdin = open("9328_열쇠.txt")


def bfs():
    global keys, flag, count
    deq = collections.deque()
    for i in range(len(starts)):
        deq.append(starts[i])
    while deq:
        x, y, = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N+2 and 0 <= ny < M+2:
                if visited[nx][ny] == 0:
                    if G[nx][ny] == '.':
                        deq.append([nx, ny])
                        visited[nx][ny] = 1
                    elif 65 <= ord(G[nx][ny]) <= 90:
                        if chr(ord(G[nx][ny]) + 32) in keys:
                            deq.append([nx, ny])
                            visited[nx][ny] = 1
                            G[nx][ny] = '.'
                            flag = 1
                    elif 97 <= ord(G[nx][ny]) <= 122:
                        deq.append([nx, ny])
                        visited[nx][ny] = 1
                        keys.append(G[nx][ny])
                        G[nx][ny] = '.'
                        flag = 1
                    elif G[nx][ny] == '$':
                        deq.append([nx, ny])
                        visited[nx][ny] = 1
                        keys.append(G[nx][ny])
                        G[nx][ny] = '.'
                        count += 1
                        flag = 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    G = [list(input()) for _ in range(N)]
    visited = [[0 for _ in range(M+2)] for _ in range(N+2)]
    G.insert(0, ['.']*(M+2))
    G.append(['.'] * (M + 2))
    for i in range(1, N+1):
        G[i].insert(0, '.')
        G[i].append('.')
    keys = list(input())
    count = 0
    if keys[0] == '0':
        keys.pop()
    starts = [[0, 0]]
    if len(starts) == 0:
        print(0)
    else:
        flag = 1
        while 1:
            if flag == 0:
                break
            visited = [[0 for _ in range(M+2)] for _ in range(N+2)]
            for start in starts:
                visited[start[0]][start[1]] = 1
            flag = 0
            bfs()
        print(count)





