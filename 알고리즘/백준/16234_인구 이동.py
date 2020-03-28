import sys, collections
sys.stdin = open("16234_인구 이동.txt")

def bfs(x, y):
    visited[x][y] = m
    deq = collections.deque()
    deq.append([x, y])
    while deq:
        tx, ty = deq.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if L <= abs(countries[nx][ny] - countries[tx][ty]) <= R and visited[nx][ny] == 0:
                    visited[nx][ny] = m
                    deq.append([nx, ny])


N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = 0
while 1:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    m = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<N:
                    if L<=abs(countries[nx][ny] - countries[i][j])<=R and visited[i][j] == 0:
                        m += 1
                        bfs(i, j)
                        break
    if sum(sum(visited, [])) == 0:
        break
    avg = []
    for d in range(1, m+1):
        cnt = 0
        hap = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == d:
                    cnt += 1
                    hap += countries[i][j]
        avg.append(int(hap/cnt))
    for d in range(1, m+1):
        for i in range(N):
            for j in range(N):
                if visited[i][j] == d:
                    countries[i][j] = avg[d-1]
    n += 1
print(n)