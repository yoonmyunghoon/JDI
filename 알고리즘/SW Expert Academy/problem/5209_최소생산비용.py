import sys
sys.stdin = open("5209_최소생산비용.txt")

def perm(n, k, Sum):
    global Min
    if Min <= Sum:
        return
    if n == k:
        if Min > Sum:
            Min = Sum
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1, Sum + data[k][arr[k]])
            arr[i], arr[k] = arr[k], arr[i]

T =int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    Min = 99*N*N
    perm(N, 0, 0)
    print('#{} {}'.format(tc, Min))
