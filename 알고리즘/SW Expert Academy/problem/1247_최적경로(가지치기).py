import sys
sys.stdin = open("1247_최적경로.txt")

def calc(v, w):
    return abs(v[0] - w[0]) + abs(v[1] - w[1])

def perm(n, k, distance):
    global mindistance
    if mindistance <= distance:
        return
    if n == k:
        distance += calc(customer[order[k - 1]], customer[order[k]])
        if distance < mindistance:
            mindistance = distance
    else:
        for i in range(k, n):
            order[i], order[k] = order[k], order[i]
            perm(n, k + 1, distance + calc(customer[order[k - 1]], customer[order[k]]))
            order[i], order[k] = order[k], order[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    company = [data.pop(0), data.pop(0)]
    home = [data.pop(0), data.pop(0)]
    customer = [[data[2*i], data[2*i+1]] for i in range(N)]
    customer.insert(0, company)
    customer.append(home)
    order = list(range(N+2))
    mindistance = 200*(N+1)
    perm(N+1, 1, 0)
    print('#{} {}'.format(tc, mindistance))