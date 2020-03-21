import sys
sys.stdin = open("스티커 붙이기.txt")

N, M, K = map(int, input().split())
notebook = [[0 for _ in range(M)] for _ in range(N)]
stikers = []
for i in range(K):
    x, y = map(int, input().split())
    stiker = [list(map(int, input().split())) for _ in range(x)]
    stikers.append(stiker)

def compare(i, a, b, hap):
    cnt = 0
    for x in range(len(stikers[i])):
        for y in range(len(stikers[i][0])):
            if stikers[i][x][y] + notebook[a + x][b + y] == 2:
                return 0
            else:
                cnt += 1
    if hap == cnt:
        return 1

for i in range(K):
    hap = len(stikers[i]) * len(stikers[i][0])
    attached = 0
    change_cnt = 0
    while 1:
        if len(stikers[i]) <= N and len(stikers[i][0]) <= M:
            for a in range(N-len(stikers[i])+1):
                if attached == 1:
                    break
                for b in range(M-len(stikers[i][0])+1):
                    if attached == 1:
                        break
                    if compare(i, a, b, hap) == 0:
                        continue
                    else:
                        for x in range(len(stikers[i])):
                            for y in range(len(stikers[i][0])):
                                if stikers[i][x][y] == 1:
                                    notebook[a + x][b + y] = stikers[i][x][y]
                        attached = 1
        if attached == 0:
            if change_cnt == 3:
                break
            change_cnt += 1
            change_stiker = []
            for a in range(len(stikers[i][0])):
                ww = []
                for b in range(len(stikers[i])-1, -1, -1):
                    ww.append(stikers[i][b][a])
                change_stiker.append(ww)
            stikers[i] = change_stiker
        else:
            break
result = 0
for i in range(len(notebook)):
    for j in range(len(notebook[i])):
       if notebook[i][j] == 1:
           result += 1
print(result)

