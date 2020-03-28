import sys
sys.stdin = open("1937_욕심쟁이 판다.txt")

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
check1 = [[0]*n for _ in range(n)]
check2 = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if forest[i][j] > forest[nx][ny]:
                    check1[i][j] = 1
                    break

for i in check1:
    print(i)
def counter(p):
    if p % 2 == 1:
        for a in range(n):
            for b in range(n):
                if check1[a][b] == 1:
                    return 1
    elif p % 2 == 0:
        for a in range(n):
            for b in range(n):
                if check2[a][b] == 1:
                    return 1
    return 0

K = 1
while 1:
    if K % 2 == 1:
        for i in range(n):
            for j in range(n):
                if check1[i][j] == 1:
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and check1[nx][ny] == 1:
                            if forest[i][j] > forest[nx][ny]:
                                check2[i][j] = 1
                                break
                    else:
                        check2[i][j] = 0
                else:
                    check2[i][j] = 0
    else:
        for i in range(n):
            for j in range(n):
                if check2[i][j] == 1:
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and check2[nx][ny] == 1:
                            if forest[i][j] > forest[nx][ny]:
                                check1[i][j] = 1
                                break
                    else:
                        check1[i][j] = 0
                else:
                    check1[i][j] = 0
    if counter(K) == 0:
        break
    K += 1
print(K)