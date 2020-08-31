import sys
sys.stdin = open("1780_종이의 개수.txt")


def check(x1, y1, x2, y2):
    global m_one, zero, p_one
    if x2 - x1 < 0:
        return
    temp = paper[x1-1][y1-1]
    flag = 1
    for i in range(x1-1, x2):
        if flag == 0:
            break
        for j in range(y1-1, y2):
            if paper[i][j] != temp:
                flag = 0
                break
    if flag == 1:
        if temp == -1:
            m_one += 1
        elif temp == 0:
            zero += 1
        else:
            p_one += 1
        return

    diff = (x2 - x1 + 1) // 3
    for n in range(3):
        for m in range(3):
            check(x1 + n * diff, y1 + m * diff, x1 + (n+1) * diff - 1, y1 + (m+1) * diff - 1)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
m_one = 0
zero = 0
p_one = 0
check(1, 1, N, N)
print(m_one)
print(zero)
print(p_one)