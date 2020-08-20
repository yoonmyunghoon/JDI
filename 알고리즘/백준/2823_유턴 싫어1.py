import sys
sys.stdin = open("2823_유턴 싫어.txt")


def check():
    for i in range(R):
        for j in range(C):
            if Town[i][j] == '.':
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and Town[nx][ny] == '.':
                        cnt += 1
                if cnt <= 1:
                    return 1
    return 0


R, C = map(int, input().split())
Town = [list(input()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(check())


