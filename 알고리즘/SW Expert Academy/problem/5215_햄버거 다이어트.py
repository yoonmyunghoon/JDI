import sys
sys.stdin = open("5215_햄버거 다이어트.txt")

def comb(n, r, s, cal):
    global maxs, mincal
    if cal > mincal:
        return
    if r == 0:
        if s >= maxs and cal <= mincal:
            maxs = s
            mincal = cal
    elif n < r:
        return
    else:
        T[r-1] = ing[n-1]
        comb(n-1, r-1, s+ing[n-1][0], cal+ing[n-1][1])
        comb(n-1, r, s, cal)

T = int(input())
for tc in range(1, T+1):
    N, limit = map(int, input().split())
    ing = []
    for i in range(N):
        ing.append(list(map(int, input().split())))
    # print(ing)
    maxs = 0
    mincal = limit
    for r in range(1, N+1):
        T = [0]*r
        comb(N, r, 0, 0)
        print()
    print(mincal)
    print(maxs)