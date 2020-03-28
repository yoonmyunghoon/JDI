import sys
sys.stdin = open("2823_유턴 싫어.txt")

def check():
    for i in range(R):
        for j in range(C):
            if city[i][j] == '.':
                n = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 > nx or nx >= R or 0 > ny or ny >= C:
                        n += 1
                    elif city[nx][ny] == 'X':
                        n += 1
                if n == 3:
                    return 1
    return 0

R, C = map(int, input().split())
city = [list(input()) for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
print(check())