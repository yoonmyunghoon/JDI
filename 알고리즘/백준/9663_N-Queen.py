import sys
sys.stdin = open("9663_N-Queen.txt")


def check(y):
    for j in range(1, y):
        if X[j] == X[y] or abs(X[j] - X[y]) == y - j:
            return 0
    return 1


def counter(y):
    global cnt
    if y == N+1:
        cnt += 1
        return
    for k in range(1, N+1):
        X[y] = k
        if check(y):
            counter(y+1)


N = int(input())
cnt = 0
X = [0]*(N+1)
counter(1)
print(cnt)
