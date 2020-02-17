import sys
sys.stdin = open("전자카트.txt")

def perm(n, k, before, s):
    global Min
    if Min <= s:
        return
    if n == k:
        s += data[before][0]
        if Min > s:
            Min = s
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1, arr[k], s+data[before][arr[k]])
            arr[i], arr[k] = arr[k], arr[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(1, N))
    Min = N*100
    perm(N-1, 0, 0, 0)
    print('#{} {}'.format(tc, Min))