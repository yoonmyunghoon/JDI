import sys
sys.stdin = open("11729_하노이 탑 이동 순서.txt")


def moving(n, a, b):
    if n == 1:
        print(a, b)
    else:
        moving(n-1, a, 6-(a+b))
        print(a, b)
        moving(n-1, 6-(a+b), b)


N = int(input())
# count = 1
# for n in range(1, N+1):
#     if n == N:
#         print(count)
#     else:
#         count = 2*count+1
print(2**N-1)
moving(N, 1, 3)


