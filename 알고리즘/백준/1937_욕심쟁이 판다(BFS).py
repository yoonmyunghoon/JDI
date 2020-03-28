import sys, collections
sys.stdin = open("1937_욕심쟁이 판다.txt")

def bfs(x, y):
    deq = collections.deque()
    deq.append([x, y, 1])
    max_d = 0
    while deq:
        tx, ty, d = deq.popleft()
        if max_d < d:
            max_d = d
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < n and 0 <= ny < n and forest[tx][ty] < forest[nx][ny]:
                if check[nx][ny]:
                    if max_d < check[nx][ny] + d:
                        max_d = check[nx][ny] + d
                else:
                    deq.append([nx, ny, d+1])
    check[x][y] = max_d
n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    for j in range(n):
        bfs(i, j)
        print([i, j])
        for k in check:
            print(k)
        print()

maximun = 0
for i in check:
    if maximun < max(i):
        maximun = max(i)
print(maximun)