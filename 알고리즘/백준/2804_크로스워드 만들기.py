import sys
sys.stdin = open("2804_크로스워드 만들기.txt")


def findposition():
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return i, j


A, B = map(str, input().split())
py, px = findposition()

data = [['.' for _ in range(len(A))] for _ in range(len(B))]
for a in range(len(A)):
    data[px][a] = A[a]
for b in range(len(B)):
    data[b][py] = B[b]
for i in range(len(B)):
    for j in range(len(A)):
        print(data[i][j], end='')
    print()

