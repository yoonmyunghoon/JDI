import sys, collections
sys.stdin = open("17822_원판돌리기.txt")

def check(x, y):
    global flag1, visited
    visited[x][y] = 1
    deq = collections.deque()
    deq.append([x, y])
    flag = 0
    while deq:
        tx, ty = deq.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = (ty + dy[i])%M
            if 0 <= nx < N and 0 <= ny < M:
                if onepan[nx][ny] == onepan[x][y] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    onepan[nx][ny] = 0
                    flag = 1
                    deq.append([nx, ny])
    if flag == 1:
        flag1 = 1
        onepan[x][y] = 0
    else:
        visited[x][y] = 0

N, M, T = map(int, input().split())
onepan = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
changes = []
flag1 = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(T):
    x, d, k = map(int, input().split())
    changes.append([x, d, k])

for i in range(len(changes)):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    flag1 = 0
    for j in range(1, len(onepan)+1):
        if j%changes[i][0] == 0:
            if changes[i][1] == 0:
                for k in range(changes[i][2]):
                    a = onepan[j-1].pop()
                    onepan[j-1].insert(0, a)
            else:
                for k in range(changes[i][2]):
                    a = onepan[j-1].pop(0)
                    onepan[j-1].insert(M-1, a)

    for v in range(N):
        for w in range(M):
            if onepan[v][w] != 0 and visited[v][w] == 0:
                check(v, w)
    if flag1 == 0:
        hap = 0
        cnt = 0
        for x1 in range(N):
            for y1 in range(M):
                if onepan[x1][y1] != 0:
                    hap += onepan[x1][y1]
                    cnt += 1
        if cnt != 0:
            avg = hap/cnt
            for x2 in range(N):
                for y2 in range(M):
                    if onepan[x2][y2] != 0:
                        if onepan[x2][y2] > avg:
                            onepan[x2][y2] -= 1
                        elif onepan[x2][y2] < avg:
                            onepan[x2][y2] += 1
hap = 0
for x in range(N):
    for y in range(M):
        if onepan[x][y] != 0:
            hap += onepan[x][y]
print(hap)
