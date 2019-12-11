import sys
sys.stdin = open("1247_최적경로.txt")

def calc(v, w):
    return abs(v[0] - w[0]) + abs(v[1] - w[1])

def perm(n, k):
    global mindistance
    if n == k:
        distance = calc(company, customer[order[0]])
        for i in range(n-1):
            distance += calc(customer[order[i]], customer[order[i+1]])
        distance += calc(customer[order[n-1]], home)
        if mindistance > distance:
            mindistance = distance
        # print(order)
    else:
        for i in range(k, n):
            order[i], order[k] = order[k], order[i]
            perm(n, k+1)
            order[i], order[k] = order[k], order[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    company = [data.pop(0), data.pop(0)]
    home = [data.pop(0), data.pop(0)]
    customer = [[data[2*i], data[2*i+1]] for i in range(N)]
    order = list(range(N))
    mindistance = 200*(N+1)
    perm(N, 0)
    print('#{} {}'.format(tc, mindistance))
