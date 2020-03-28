import sys, collections
sys.stdin = open("3190_뱀.txt")

N = int(input())
K = int(input())
G = [[0 for _ in range(N)] for _ in range(N)]
changeD = []
for i in range(K):
    r, c = map(int, input().split())
    G[r-1][c-1] = 1
L = int(input())
for i in range(L):
    X, C = map(str, input().split())
    changeD.append([int(X), C])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
bam = collections.deque()
bam.append([0, 0])
x, y = 0, 0
t = 0
d = 0
p = 0
while 1:
    if p < len(changeD):
        if t == changeD[p][0]:
            if changeD[p][1] == 'D':
                d = (d + 1)%4
            else:
                d = (d + 3)%4
            p += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 > nx or nx >= N or 0 > ny or ny >= N or [nx, ny] in bam:
        break
    if G[nx][ny] == 1:
        G[nx][ny] = 2
        bam.append([nx, ny])
    else:
        G[nx][ny] = 2
        bam.append([nx, ny])
        a, b = bam.popleft()
        G[a][b] = 0
    x, y = nx, ny
    t += 1
print(t+1)