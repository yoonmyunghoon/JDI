import sys
sys.stdin = open("input.txt")
T = int(input())

def getD(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def calc():
    global ans
    dist = 0
    for i in range(n-1):
        dist += getD(customer[A[i]], customer[A[i+1]])
    dist += getD(company, customer[A[0]])
    dist += getD(customer[A[n-1]], home)
    if ans > dist:
        ans = dist

def perm(n, k):
    if n == k:
        calc()
    else:
        for i in range(k, n):
            A[i], A[k] = A[k], A[i]
            perm(n, k+1)
            A[i], A[k] = A[k], A[i]

for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    A = list(range(n))
    company = (data[0], data[1])
    home = (data[2], data[3])
    customer = []
    for i in range(4, len(data), 2):
        customer.append((data[i], data[i+1]))
    ans = 2000
    perm(n, 0)
    print('#{} {}'.format(tc, ans))

