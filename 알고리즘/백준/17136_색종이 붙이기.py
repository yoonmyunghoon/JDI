import sys
sys.stdin = open("17136_색종이 붙이기.txt")


def change(n, x, y, color):
    for i in range(x, x+n):
        for j in range(y, y+n):
            paper[i][j] = color


def checking(n, x, y):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] == 0:
                return 0
    return 1


def find_position():
    for i in range(10):
        for j in range(10):
            if paper[i][j]:
                return i, j
    return -1, -1


def attach(cnt):
    global space, result
    if cnt >= result:
        return
    if space == 0:
        if result > cnt:
            result = cnt
        return
    x, y = find_position()
    if x != -1:
        for s in range(1, 6):
            if counts[s] > 0:
                if 0 <= x <= 10-s and 0 <= y <= 10-s:
                    if checking(s, x, y):
                        counts[s] -= 1
                        space -= s ** 2
                        change(s, x, y, 0)
                        attach(cnt+1)
                        change(s, x, y, 1)
                        space += s ** 2
                        counts[s] += 1


paper = [list(map(int, input().split())) for _ in range(10)]
space = 0
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            space += 1
counts = [0, 5, 5, 5, 5, 5]
result = 987654321
attach(0)
if result == 987654321:
    print(-1)
else:
    print(result)

