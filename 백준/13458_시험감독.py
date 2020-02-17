import sys
sys.stdin = open("13458_시험감독.txt")

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in range(len(A)):
    if A[i] > B:
        cnt += 1
        A[i] -= B
    else:
        cnt += 1
        A[i] = 0
for i in range(len(A)):
    if A[i]%C==0:
        cnt += A[i]//C
    else:
        cnt += (A[i]//C + 1)
print(cnt)

