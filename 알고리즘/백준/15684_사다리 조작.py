import sys, copy
sys.stdin = open("15684_사다리 조작.txt")


def comb(n, r):
    if result != -1:
        return
    if r == 0:
        check(T)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


def check(T):
    global result
    sadari_c = copy.deepcopy(sadari)
    cnt = 0
    for t in T:
        if sadari_c[checking[t][0]][checking[t][1]] == 0:
            sadari_c[checking[t][0]][checking[t][1]] = 1
            sadari_c[checking[t][0]][checking[t][1]+1] = 2
            cnt += 1
        else:
            return
    if cnt == len(T):
        flag = 1
        for i in range(1, N+1):
            if flag == 0:
                break
            x = 1
            y = i
            while 1:
                if flag == 0:
                    break
                if sadari_c[x][y] == 1:
                    x = x+dx[2]
                    y = y+dy[2]
                elif sadari_c[x][y] == 2:
                    x = x+dx[1]
                    y = y+dy[1]
                else:
                    x = x+dx[0]
                    y = y+dy[0]
                if x == H+1:
                    if y != i:
                        flag = 0
                    break
        if flag == 1:
            result = len(T)


N, M, H = map(int, input().split())
sadari = [[0 for _ in range(N+1)] for _ in range(H+1)]
IMPOS = []
result = -1
dx = [1, 1, 1]
dy = [0, -1, 1]
for i in range(M):
    a, b = map(int, input().split())
    sadari[a][b] = 1
    sadari[a][b+1] = 2
    IMPOS.append([a, b])
    if b == 1:
        IMPOS.append([a, b+1])
    elif b == N-1:
        IMPOS.append([a, b-1])
    else:
        IMPOS.append([a, b-1])
        IMPOS.append([a, b+1])

checking = []
for i in range(1, H+1):
    for j in range(1, N):
        if [i, j] not in IMPOS:
            checking.append([i, j])

for cnt in range(0, 4):
    if result != -1:
        break
    A = range(len(checking))
    T = [0] * cnt
    comb(len(checking), cnt)
print(result)