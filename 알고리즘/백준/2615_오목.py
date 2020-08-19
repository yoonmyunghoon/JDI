import sys
sys.stdin = open("2615_오목.txt")


def game():
    global result, rx, ry
    for j in range(19):
        for i in range(19):
            if data[i][j] != 0:
                cnt = 1
                s = data[i][j]
                nx, ny = i, j
                for d in direction[i][j]:
                    while 1:
                        nx = nx + dx[d]
                        ny = ny + dy[d]
                        if 0 <= nx < 19 and 0 <= ny < 19 and data[nx][ny] == s:
                            direction[nx][ny].remove(d)
                            cnt += 1
                        else:
                            break
                    if cnt == 5:
                        result = s
                        rx, ry = i, j
                        return
                    else:
                        cnt = 1
                        nx, ny = i, j


data = [list(map(int, input().split())) for _ in range(19)]
direction = [[[0, 1, 2, 3] for _ in range(19)] for _ in range(19)]
dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]
result = 0
rx, ry = 0, 0
game()
if result > 0:
    print(result)
    print(rx+1, ry+1)
else:
    print(result)



