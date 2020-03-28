import sys
sys.stdin = open("1937_욕심쟁이 판다.txt")

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if forest[i][j] > forest[nx][ny]:
                    check[i][j] = 1
                    break

# for i in check:
#     print(i)

def counter(p):
    for a in range(n):
        for b in range(n):
            if check[a][b] == p:
                return 1
    return 0

K = 1
while 1:
    for i in check:
        print(i)
    for i in range(n):
        for j in range(n):
            if check[i][j] == K:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and check[nx][ny] >= K:
                        if forest[i][j] > forest[nx][ny]:
                            check[i][j] += 1
                            break
    if counter(K) == 0:
        break
    K += 1
print(K)