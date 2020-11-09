# 순열

# 라이브러리 x

# 1. N개 순서 세우기 => N!
N = 4
arr = [1, 2, 3, 4]
#
# def perm(n, k):
#     if n == k:
#         print(arr)
#     else:
#         for i in range(k, n):
#             arr[i], arr[k] = arr[k], arr[i]
#             perm(n, k+1)
#             arr[i], arr[k] = arr[k], arr[i]
#
# perm(N, 0)

# 2. n개 중에서 r개를 뽑아서 순서세우기 => nCr
R = 3
P = [0]*R

# def perm1(n, r):
#     if r == 0:
#         print(P)
#     else:
#         for i in range(n-1, -1, -1):
#             arr[i], arr[n-1] = arr[n-1], arr[i]
#             P[r-1] = arr[n-1]
#             perm1(n-1, r-1)
#             arr[i], arr[n - 1] = arr[n - 1], arr[i]
# perm1(N, R)

# 3. n개 중에서 r개를 뽑는데 중복을 허용함

# def perm2(n, r):
#     if r == 0:
#         print(P)
#     else:
#         for i in range(n-1, -1, -1):
#             arr[i], arr[n-1] = arr[n-1], arr[i]
#             P[r-1] = arr[n-1]
#             perm2(n, r-1)
#             arr[i], arr[n - 1] = arr[n - 1], arr[i]
#
# perm2(N, R)

# 라이브러리 o
from itertools import permutations
print(list(permutations(arr, 3)))

from itertools import product
print(list(product(arr, repeat=3)))