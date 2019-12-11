import sys, collections
sys.stdin = open("4179_불!.txt")

def bfs(x, y, fire):
    global result, result1
    visited[x][y] = 0
    Fire = collections.deque()
    JiHoon = collections.deque()
    for i in range(len(fire)):
        Fire.append((fire[i][0], fire[i][1]))
    JiHoon.append((x, y))
    arr = []
    for i in range(len(Fire)):
        arr.append(Fire[i])
    arr1 = []
    arr1.append((x, y))
    check = 0
    if len(arr) == 0:
        check = 1
    while 1:
        if check == 0:
            while 1:
                if len(Fire) == 0:
                    result = -1
                    return
                if Fire[0] not in arr:
                    break
                ta, tb = Fire.popleft()
                for i in range(4):
                    na = ta + dx[i]
                    nb = tb + dy[i]
                    if 0 <= na < R and 0 <= nb < C:
                        if G[na][nb] != '#' and G[na][nb] != 'F':
                            G[na][nb] = 'F'
                            Fire.append((na, nb))
            arr = []
            for i in range(len(Fire)):
                arr.append(Fire[i])
        while 1:
            if len(JiHoon) == 0:
                result = -1
                return
            if JiHoon[0] not in arr1:
                break
            tx, ty = JiHoon.popleft()
            for i in range(4):
                nx = tx + dx[i]
                ny = ty + dy[i]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    result1.append(visited[tx][ty] + 1)
                    return
                if G[nx][ny] == '.' and visited[nx][ny] == 0:
                    G[nx][ny] = 'J'
                    visited[nx][ny] = visited[tx][ty] + 1
                    JiHoon.append((nx, ny))
        arr1 = []
        for i in range(len(JiHoon)):
            arr1.append(JiHoon[i])

R, C = map(int, input().split())
G = [list(map(str, input())) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
result = 0
result1 = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
JH = []
FIRE = []
for i in range(R):
    for j in range(C):
        if G[i][j] == 'J':
            JH = [i, j]
        if G[i][j] == 'F':
            FIRE.append([i, j])
bfs(JH[0], JH[1], FIRE)
if result == -1:
    print('IMPOSSIBLE')
else:
    print(min(result1))



