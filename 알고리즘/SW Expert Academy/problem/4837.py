A = list(range(1, 13))
n = len(A)
S = []
for i in range(1<<n):
    L = []
    for j in range(n):
        if i&(1<<j):
            L.append(A[j])
    S.append(L)
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    cnt = 0
    for i in S:
        if len(i) == N and sum(i) == K:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))

