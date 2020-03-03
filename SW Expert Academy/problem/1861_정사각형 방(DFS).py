import sys
sys.stdin = open('1861_정사각형 방.txt')

def dfs(x, y, c):
    global cnt
    visited[x][y] = c
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and A[x][y] + 1 == A[nx][ny] and visited[nx][ny] != c:
            dfs(nx, ny, c)
            break
    else:
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    check = 0
    maximum = 0
    minimumnum = 987654321
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt = 0
                check += 1
                dfs(i, j, check)
                if maximum < cnt:
                    maximum = cnt
                    minimumnum = A[i][j]
                elif maximum == cnt:
                    if minimumnum > A[i][j]:
                        minimumnum = A[i][j]
    print('#{} {} {}'.format(tc, minimumnum, maximum))
