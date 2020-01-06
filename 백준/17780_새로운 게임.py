import sys
sys.stdin = open("17780_새로운 게임.txt")
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
def change(n):
    for i in range(len(mals)):
        if mals[i][0][0] == n:
            nx = mals[i][0][1] + dx[mals[i][0][3]]
            ny = mals[i][0][2] + dy[mals[i][0][3]]
            if nx == -1 or nx == N or ny == -1 or ny == N or chesspan[nx][ny] == 2:
                if mals[i][0][3] == 1: mals[i][0][3] = 0
                elif mals[i][0][3] == 0: mals[i][0][3] = 1
                elif mals[i][0][3] == 2: mals[i][0][3] = 3
                else: mals[i][0][3] = 2
                nx = mals[i][0][1] + dx[mals[i][0][3]]
                ny = mals[i][0][2] + dy[mals[i][0][3]]
                if nx == -1 or nx == N or ny == -1 or ny == N or chesspan[nx][ny] == 2:
                    return
                elif chesspan[nx][ny] == 0:
                    for a in range(len(mals)):
                        if mals[a][0][1] == nx and mals[a][0][2] == ny:
                            for b in range(len(mals[i])):
                                mals[i][b][1] = nx
                                mals[i][b][2] = ny
                                mals[a].append(mals[i][b])
                            mals.remove(mals[i])
                            return
                    else:
                        for b in range(len(mals[i])):
                            mals[i][b][1] = nx
                            mals[i][b][2] = ny
                        return
                elif chesspan[nx][ny] == 1:
                    for a in range(len(mals)):
                        if mals[a][0][1] == nx and mals[a][0][2] == ny:
                            for b in range(len(mals[i])):
                                mals[i][len(mals[i]) - b - 1][1] = nx
                                mals[i][len(mals[i]) - b - 1][2] = ny
                                mals[a].append(mals[i][len(mals[i]) - b - 1])
                            mals.remove(mals[i])
                            return
                    else:
                        for b in range(len(mals[i])):
                            mals[i][b][1] = nx
                            mals[i][b][2] = ny
                        for c in range(len(mals[i]) // 2):
                            mals[i][c], mals[i][len(mals[i]) - c - 1] = mals[i][len(mals[i]) - c - 1], mals[i][c]
                        return
            elif chesspan[nx][ny] == 0:
                for a in range(len(mals)):
                    if mals[a][0][1] == nx and mals[a][0][2] == ny:
                        for b in range(len(mals[i])):
                            mals[i][b][1] = nx
                            mals[i][b][2] = ny
                            mals[a].append(mals[i][b])
                        mals.remove(mals[i])
                        return
                else:
                    for b in range(len(mals[i])):
                        mals[i][b][1] = nx
                        mals[i][b][2] = ny
                    return
            elif chesspan[nx][ny] == 1:
                for a in range(len(mals)):
                    if mals[a][0][1] == nx and mals[a][0][2] == ny:
                        for b in range(len(mals[i])):
                            mals[i][len(mals[i]) - b - 1][1] = nx
                            mals[i][len(mals[i]) - b - 1][2] = ny
                            mals[a].append(mals[i][len(mals[i]) - b - 1])
                        mals.remove(mals[i])
                        return
                else:
                    for b in range(len(mals[i])):
                        mals[i][b][1] = nx
                        mals[i][b][2] = ny
                    for c in range(len(mals[i]) // 2):
                        mals[i][c], mals[i][len(mals[i]) - c - 1] = mals[i][len(mals[i]) - c - 1], mals[i][c]
                    return

N, K = map(int, input().split())
# 0: 흰색, 1: 빨간색, 2: 파란색
chesspan = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
mals = []
for i in range(K):
    x, y, d = map(int, input().split())
    # [[번호, x좌표, y좌표, 방향]]
    mals.append([[i, x-1, y-1, d-1]])
# print(N, K)
# for i in chesspan:
#     print(i)
# print(mals)
# print(len(mals))
# print("===================================")
t = 0
h = 0
while len(mals) > 1:
    if t > 1000:
        t = -1
        break
    for k in range(len(mals)):
        if len(mals[k]) > h:
            h = len(mals[k])
    if h >= 4:
        break
    t += 1
    n = -1
    while n < K-1:
        n += 1
        change(n)
    # print(t)
    # for m in mals:
    #     for z in m:
    #         print([z[1]+1, z[2]+1, z[3]+1, z[0]+1], end=' ')
    #     print()
    # print()
print(t)