import sys
sys.stdin = open("3109_빵집.txt")


def make_pipe(d, x, y):
    global cnt, flag
    if flag == 1:
        return
    if d == C-1 and Map[x][y] == '.':
        Map[x][y] = 'x'
        cnt += 1
        flag = 1
        return
    Map[x][y] = 'x'
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if 0 <= nx < R and Map[nx][ny] == '.':
            make_pipe(d + 1, nx, ny)


R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]
dx = [-1, 0, 1]
cnt = 0
flag = 0
for i in range(R):
    flag = 0
    make_pipe(0, i, 0)
print(cnt)