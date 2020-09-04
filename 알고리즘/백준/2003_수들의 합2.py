import sys
sys.stdin = open("2003_수들의 합2.txt")


def counting(s, e, m):
    result = 0
    while 1:


N, M = map(int, input().split())
A = list(map(int, input().split()))
print(N, M, A)
counting(0, 0, M)