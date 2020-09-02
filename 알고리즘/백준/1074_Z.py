import sys
sys.stdin = open("1074_Z.txt")


def draw(x1, y1, n):
    global cnt, flag
    if flag == 1:
        return
    if n == 0:
        cnt += 1
        if x1 == r and y1 == c:
            flag = 1
            print(cnt)
        return
    diff = (2 ** n) // 2
    if n == N:
        draw(x1, y1, n - 1)
        draw(x1, y1 + diff, n - 1)
        draw(x1 + diff, y1, n - 1)
        draw(x1 + diff, y1 + diff, n - 1)
    else:
        if x1 <= r < x1+2*diff+1 and y1 <= c < y1+2*diff+1:
            draw(x1, y1, n - 1)
            draw(x1, y1 + diff, n - 1)
            draw(x1 + diff, y1, n - 1)
            draw(x1 + diff, y1 + diff, n - 1)
        else:
            cnt += (2**n)**2
            return


N, r, c = map(int, input().split())
cnt = -1
flag = 0
draw(0, 0, N)
