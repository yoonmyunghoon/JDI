import sys, collections
sys.stdin = open("Gaaaaaaaaaarden.txt")


def bfs():
    global visited, maximum
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    deq = collections.deque()
    for i in range(G + R):
        if selected[i] in g_position:
            deq.append([selected[i][0], selected[i][1], 'G'])
            visited[selected[i][0]][selected[i][1]] = ['G', 1]
    for i in range(G + R):
        if selected[i] not in g_position:
            deq.append([selected[i][0], selected[i][1], 'R'])
            visited[selected[i][0]][selected[i][1]] = ['R', 1]
    while deq:
        x, y, t = deq.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<M and garden[nx][ny] != 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = [t, visited[x][y][1] + 1]
                    deq.append([nx, ny, t])
                else:
                    if visited[x][y][0] == 'R' and visited[nx][ny][0] == 'G' and visited[nx][ny][1] == visited[x][y][1] + 1:
                        cnt += 1
                        print(visited[nx][ny])
                        visited[nx][ny] = ['S', 0]

    if maximum < cnt:
        maximum = cnt


def comb1(n, r):
    if r == 0:
        bfs()
    elif r > n:
        return
    else:
        g_position[r-1] = selected[n-1]
        comb1(n-1, r-1)
        comb1(n-1, r)


def comb(n, r):
    if r == 0:
        comb1(G+R, G)
    elif r > n:
        return
    else:
        selected[r-1] = available_position[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
available_position = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            available_position.append([i, j])

selected = [0]*(G+R)
g_position = [0] * G
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maximum = 0
comb(len(available_position), G+R)
print(maximum)
