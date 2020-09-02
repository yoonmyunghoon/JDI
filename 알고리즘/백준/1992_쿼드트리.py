import sys
sys.stdin = open("1992_쿼드트리.txt")


def press(x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return
    check = data[x1-1][y1-1]
    flag = 0
    for x in range(x1-1, x2):
        if flag == 1:
            break
        for y in range(y1-1, y2):
            if data[x][y] != check:
                flag = 1
                break
    if flag == 1:
        diff = (x2 - x1 + 1)//2
        print('(', end='')
        for i in range(2):
            for j in range(2):
                press(x1 + i * diff, y1 + j * diff, x1 + (i+1) * diff - 1, y1 + (j+1) * diff - 1)
        print(')', end='')
    else:
        print(check, end='')


N = int(input())
data = [list(map(int, input())) for _ in range(N)]
press(1, 1, N, N)