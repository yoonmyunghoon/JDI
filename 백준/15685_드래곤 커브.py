import sys
sys.stdin = open("15685_드래곤 커브.txt")

N = int(input())
positions = []
for i in range(N):
    x, y, d, g = map(int, input().split())
    dragons = [[x, y]]
    if d == 0: dragons.append([x+1, y])
    elif d == 1: dragons.append([x, y-1])
    elif d == 2: dragons.append([x-1, y])
    elif d == 3: dragons.append([x, y+1])
    n = 0
    while n < g:
        n += 1
        tmp = []
        for i in range(len(dragons)-1):
            if i == 0:
                ny = dragons[-1][1] - (dragons[-1][0] - dragons[-2][0])
                nx = dragons[-1][0] + (dragons[-1][1] - dragons[-2][1])
            else:
                ny = tmp[i-1][1] - (dragons[-(i+1)][0] - dragons[-(i+1)-1][0])
                nx = tmp[i-1][0] + (dragons[-(i+1)][1] - dragons[-(i+1)-1][1])
            tmp.append([nx, ny])
        dragons += tmp
    positions += dragons
graph = [[0]*101 for _ in range(101)]
for i in range(len(positions)):
    graph[positions[i][0]][positions[i][1]] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            cnt += 1
print(cnt)


