import sys
sys.stdin = open("input.txt")
T = int(input())

def getDis(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def calcDis():
    global result
    dis = 0
    for i in range(n-1):
        dis += getDis(customer[A[i]], customer[A[i+1]])
    dis += getDis(company, customer[A[0]])
    dis += getDis(customer[A[-1]], home)
    if result > dis:
        result = dis

def perm(n, k):
    if n == k:
        calcDis()
    else:
        for i in range(k, n):
            A[i], A[k] = A[k], A[i]
            perm(n, k+1)
            A[i], A[k] = A[k], A[i]

for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    company = [data[0], data[1]]
    home = [data[2], data[3]]
    A = list(range(n))
    customer = []
    for i in range(4, len(data), 2):
        customer.append([data[i], data[i+1]])
    result = 2000
    perm(n, 0)
    print('#{} {}'.format(tc, result))