import sys
sys.stdin = open("15684_사다리 조작.txt")


# def comb(n, r):
#     if r == 0:
#         print(T)
#         # check(T)
#     elif n < r:
#         return
#     else:
#         T[r-1] = A[n-1]
#         comb(n-1, r-1)
#         comb(n-1, r)


# def check(T):



N, M, H = map(int, input().split())
sadari = [[0 for _ in range(N+1)] for _ in range(H+1)]
IMPOS = []
for i in range(M):
    a, b = map(int, input().split())
    sadari[a][b] = 1
    sadari[a][b+1] = 2
    IMPOS.append([a, b])
    if b == 1:
        IMPOS.append([a, b+1])
    elif b == N-1:
        IMPOS.append([a, b-1])
    else:
        IMPOS.append([a, b-1])
        IMPOS.append([a, b+1])

for i in sadari:
    print(i)
print()

checking = []
for i in range(1, H+1):
    for j in range(1, N):
        if [i, j] not in IMPOS:
            checking.append([i, j])

for i in checking:
    print(i)
print()


# for cnt in range(1, 4):
#     A = range(len(checking))
#     T = [0] * cnt
#     comb(len(checking), cnt)
#     print()