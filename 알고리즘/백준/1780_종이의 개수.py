import sys
sys.stdin = open("1780_종이의 개수.txt")


def check(x1, y1, x2, y2):
    global m_one, zero, p_one
    if x2 - x1 == 0:
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
    check(1, 1, x2 // 3, y2 // 3)
    check((x2 // 3) + 1, 1, (x2 // 3) * 2, y2 // 3)
    check((x2 // 3) * 2 + 1, 1, x2, y2 // 3)

    check(1, (y2 // 3) + 1, x2 // 3, (y2 // 3) * 2)
    check((x2 // 3) + 1, (y2 // 3) + 1, (x2 // 3) * 2, (y2 // 3) * 2)
    check((x2 // 3) * 2 + 1, (y2 // 3) + 1, x2, (y2 // 3) * 2)

    check(1, (y2 // 3) * 2 + 1, x2 // 3, y2)
    check((x2 // 3) + 1, (y2 // 3) * 2 + 1, (x2 // 3) * 2, y2)
    check((x2 // 3) * 2 + 1, (y2 // 3) * 2 + 1, x2, y2)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
for i in paper:
    print(i)
m_one = 0
zero = 0
p_one = 0
check(1, 1, 9, 9)