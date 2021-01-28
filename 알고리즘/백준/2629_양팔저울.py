import sys
sys.stdin = open("2629_양팔저울.txt")


def weight_check(n, left, right):
    w = abs(left - right)
    if n == len_chu:
        weight.add(w)
        return
    if check[w][n]:
        return
    check[w][n] = 1
    weight.add(w)
    weight_check(n + 1, left, right)
    weight_check(n + 1, left + Chu[n], right)
    weight_check(n + 1, left, right + Chu[n])


N = int(input())
Chu = list(map(int, input().split()))
M = int(input())
Goo = list(map(int, input().split()))

len_chu = len(Chu)
limit = Chu[-1]*len_chu
check = [[0]*len_chu for _ in range(limit)]
weight = set()
weight_check(0, 0, 0)

for g in Goo:
    if g in weight:
        print('Y', end=' ')
    else:
        print('N', end=' ')