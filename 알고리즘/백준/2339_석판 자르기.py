import sys
sys.stdin = open("2339_석판 자르기.txt")


def finding(d, x1, y1, x2, y2, x, y):
    if d == 'h':
        for j in range(y1, y2 + 1):
            if stone[x][j] == 2:
                return False
    if d == 'v':
        for j in range(x1, x2 + 1):
            if stone[j][y] == 2:
                return False
    return True


def slicing(d, x1, y1, x2, y2):
    tr = 0
    im = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if stone[x][y] == 2:
                tr += 1
            if stone[x][y] == 1:
                im += 1
    if tr == 0:
        return 0
    elif tr == 1 and im == 0:
        return 1
    elif tr >= 2 and im == 0:
        return 0
    count = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if stone[i][j] == 1:
                if d != 'v' and finding('h', x1, y1, x2, y2, i, j):
                    a = slicing('v', x1, y1, i - 1, y2)
                    b = slicing('v', i + 1, y1, x2, y2)
                    count += a * b
                if d != 'h' and finding('v', x1, y1, x2, y2, i, j):
                    a = slicing('h', x1, y1, x2, j - 1)
                    b = slicing('h', x1, j + 1, x2, y2)
                    count += a * b
    return count


N = int(input())
stone = [list(map(int, input().split())) for _ in range(N)]
treasure = []
impure = []
for i in range(N):
    for j in range(N):
        if stone[i][j] == 1:
            impure.append([i, j])
        if stone[i][j] == 2:
            treasure.append([i, j])
result = slicing('n', 0, 0, N-1, N-1)
if result > 0:
    print(result)
else:
    print(-1)


