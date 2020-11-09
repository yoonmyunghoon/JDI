# 부분집합

# 라이브러리 x
N = 5
arr = [1, 2, 3, 4, 5]
A = [0]*N

def powerset(n, k):
    if n == k:
        for i in range(n):
            if A[i] == 1:
                print(arr[i], end=' ')
        print()
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

powerset(N, 0)


# 라이브러리 o
from itertools import combinations

def powerset2(n):
    for i in range(1, n+1):
        print(list(combinations(arr, i)))

powerset2(N)

