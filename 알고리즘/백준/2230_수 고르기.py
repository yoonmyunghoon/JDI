import sys
sys.stdin = open("2230_수 고르기.txt")


def finding(s, e, m, d):
    result = d
    while 1:
        if e == N-1 and A[e] - A[s] < m:
            break
        if A[e] - A[s] < m:
            e += 1
        elif A[e] - A[s] == m:
            result = m
            break
        else:
            if A[e] - A[s] < result:
                result = A[e] - A[s]
            s += 1
    return result


N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()
D = A[-1] - A[0]
print(finding(0, 0, M, D))
