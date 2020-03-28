import sys, collections
sys.stdin = open("17144_미세먼지 안녕!.txt")

R, C, T = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(R)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
cleaner = []
for i in range(R):
    for j in range(C):
        if G[i][j] == -1:
            cleaner.append([i, j])
t = 0
while 1:
    checked = [[0 for _ in range(C)] for _ in range(R)]
    if t == T:
        break
    t += 1
    for i in range(R):
        for j in range(C):
            if G[i][j] > 0:
                n = 0
                degree = G[i][j]
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<R and 0<=ny<C and G[nx][ny] != -1:
                        n += 1
                        checked[nx][ny] += int(degree/5)
                checked[i][j] += degree - n*int(degree/5)
    upside = collections.deque()
    downside = collections.deque()
    usx, usy = cleaner[0][0], cleaner[0][1] + 1
    dsx, dsy = cleaner[1][0], cleaner[1][1] + 1
    usn = 0
    dsn = 0
    while usx != cleaner[0][0] or usy != cleaner[0][1]:
        upside.append(checked[usx][usy])
        if usn == 0 and usy == C-1:
            usn += 1
        if usn == 1 and usx == 0:
            usn += 1
        if usn == 2 and usy == 0:
            usn += 1
        usx += dx[usn]
        usy += dy[usn]
    while dsx != cleaner[1][0] or dsy != cleaner[1][1]:
        downside.append(checked[dsx][dsy])
        if dsn == 0 and dsy == C-1:
            dsn = 3
        if dsn == 3 and dsx == R-1:
            dsn = 2
        if dsn == 2 and dsy == 0:
            dsn = 1
        dsx += dx[dsn]
        dsy += dy[dsn]
    p1 = upside.pop()
    upside.appendleft(0)
    p2 = downside.pop()
    downside.appendleft(0)
    usx, usy = cleaner[0][0], cleaner[0][1] + 1
    dsx, dsy = cleaner[1][0], cleaner[1][1] + 1
    usn = 0
    dsn = 0
    unn = 0
    dnn = 0
    while usx != cleaner[0][0] or usy != cleaner[0][1]:
        checked[usx][usy] = upside[unn]
        if usn == 0 and usy == C-1:
            usn += 1
        if usn == 1 and usx == 0:
            usn += 1
        if usn == 2 and usy == 0:
            usn += 1
        usx += dx[usn]
        usy += dy[usn]
        unn += 1
    while dsx != cleaner[1][0] or dsy != cleaner[1][1]:
        checked[dsx][dsy] = downside[dnn]
        if dsn == 0 and dsy == C-1:
            dsn = 3
        if dsn == 3 and dsx == R-1:
            dsn = 2
        if dsn == 2 and dsy == 0:
            dsn = 1
        dsx += dx[dsn]
        dsy += dy[dsn]
        dnn += 1
    checked[cleaner[0][0]][cleaner[0][1]] = -1
    checked[cleaner[1][0]][cleaner[1][1]] = -1
    for i in range(R):
        for j in range(C):
            G[i][j] = checked[i][j]
print(sum(sum(G, []))+2)
