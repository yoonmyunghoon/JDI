import sys
sys.stdin = open("1996_지뢰찾기.txt")

N = int(input())
info = [list(input()) for _ in range(N)]
data = [['0' for _ in range(N)] for _ in range(N)]
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, -1, 0, 1, -1, 0, 1]

for i in range(N):
    for j in range(N):
        if info[i][j] != '.':
            data[i][j] = '*'
        else:
            hap = 0
            for c in range(8):
                if 0 <= i + dx[c] < N and 0 <= j + dy[c] < N:
                    if info[i + dx[c]][j + dy[c]] != '.':
                        hap += int(info[i + dx[c]][j + dy[c]])
            if hap >= 10:
                data[i][j] = 'M'
            else:
                data[i][j] = str(hap)
for i in range(N):
    for j in range(N):
        print(data[i][j], end='')
    print()