import sys
sys.stdin = open("15683_감시.txt")

# x, y: cctv 위치좌표, c: cctv의 종류, d: 방향
def inspect(x, y, c, d):
    if c == 1:
        a, b = x + dx[d], y + dy[d]
        while 0 <= a < N and 0 <= b < M and office[a][b] != 6:
            if office[a][b] != 0: inspected[a][b] = 0
            else: inspected[a][b] = 1
            a += dx[d]
            b += dy[d]
    elif c == 2:
        a1, b1 = x + dx[d], y + dy[d]
        while 0 <= a1 < N and 0 <= b1 < M and office[a1][b1] != 6:
            if office[a1][b1] != 0: inspected[a1][b1] = 0
            else: inspected[a1][b1] = 1
            a1 += dx[d]
            b1 += dy[d]
        d2 = (d + 2) % 4
        a2, b2 = x + dx[d2], y + dy[d2]
        while 0 <= a2 < N and 0 <= b2 < M and office[a2][b2] != 6:
            if office[a2][b2] != 0: inspected[a2][b2] = 0
            else: inspected[a2][b2] = 1
            a2 += dx[d2]
            b2 += dy[d2]
    elif c == 3:
        a1, b1 = x + dx[d], y + dy[d]
        while 0 <= a1 < N and 0 <= b1 < M and office[a1][b1] != 6:
            if office[a1][b1] != 0: inspected[a1][b1] = 0
            else: inspected[a1][b1] = 1
            a1 += dx[d]
            b1 += dy[d]
        d2 = (d + 1) % 4
        a2, b2 = x + dx[d2], y + dy[d2]
        while 0 <= a2 < N and 0 <= b2 < M and office[a2][b2] != 6:
            if office[a2][b2] != 0: inspected[a2][b2] = 0
            else: inspected[a2][b2] = 1
            a2 += dx[d2]
            b2 += dy[d2]
    elif c == 4:
        a1, b1 = x + dx[d], y + dy[d]
        while 0 <= a1 < N and 0 <= b1 < M and office[a1][b1] != 6:
            if office[a1][b1] != 0: inspected[a1][b1] = 0
            else: inspected[a1][b1] = 1
            a1 += dx[d]
            b1 += dy[d]
        d2 = (d + 1) % 4
        a2, b2 = x + dx[d2], y + dy[d2]
        while 0 <= a2 < N and 0 <= b2 < M and office[a2][b2] != 6:
            if office[a2][b2] != 0: inspected[a2][b2] = 0
            else: inspected[a2][b2] = 1
            a2 += dx[d2]
            b2 += dy[d2]
        d3 = (d + 2) % 4
        a3, b3 = x + dx[d3], y + dy[d3]
        while 0 <= a3 < N and 0 <= b3 < M and office[a3][b3] != 6:
            if office[a3][b3] != 0: inspected[a3][b3] = 0
            else: inspected[a3][b3] = 1
            a3 += dx[d3]
            b3 += dy[d3]
    elif c == 5:
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            while 0 <= a < N and 0 <= b < M and office[a][b] != 6:
                if office[a][b] != 0: inspected[a][b] = 0
                else: inspected[a][b] = 1
                a += dx[i]
                b += dy[i]


# n: cctv의 번호, dt: n번째 cctv의 변경 가능한 방향 개수
def save(n, dt):
    global inspected, minimum
    for i in range(1, dt+1):
        # n번째 cctv의 방향 저장하기
        directions[n] = i
        # 모든 cctv의 방향이 정해졌을 때, 감시된 부분 체크해주기
        if n+1 == len(cctv):
            for j in range(len(cctv)):
                inspect(cctv[j][0], cctv[j][1], cctv[j][2], directions[j]-1)
            # 사각지대 개수 세기
            count = 0
            for a in range(N):
                for b in range(M):
                    if inspected[a][b] == 0:
                        count += 1
            if count-walls-len(cctv) < minimum:
                minimum = count-walls-len(cctv)
            inspected = [[0 for _ in range(M)] for _ in range(N)]
            continue
        save(n+1, d_types[cctv[n+1][2]])

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
# 감시된 부분 체크해줄 2차원 배열
inspected = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# cctv 종류에 따른 변경 가능 방향 개수
d_types = [0, 4, 2, 4, 4, 1]
cctv = []
walls = 0
minimum = 987654321
for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([i, j, office[i][j]])
        if office[i][j] == 6:
            walls += 1
# 각 cctv의 방향을 나타내주기 위한 배열
directions = [0]*len(cctv)
# cctv가 존재하는 경우
if len(cctv) > 0:
    save(0, d_types[cctv[0][2]])
    print(minimum)
# cctv가 없는 경우
else:
    print(N*M-walls)
