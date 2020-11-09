# 조합

# 라이브러리 x
N = 4
R = 3
arr = [1, 2, 3, 4]
T = [0] * R

# def comb(n, r):
#     if r == 0:
#         print(T)
#     elif n < r:
#         return
#     else:
#         T[r-1] = arr[n-1]
#         comb(n-1, r-1)
#         comb(n-1, r)
# comb(N, R)

# 중복 허
# def comb1(n, r):
#     if r == 0:
#         print(T)
#     elif n == 0:
#         return
#     else:
#         T[r-1] = arr[n-1]
#         comb1(n, r-1)
#         comb1(n-1, r)
# comb1(N, R)

# 라이브러리 o
from itertools import combinations
print(list(combinations(arr, 3)))

from itertools import combinations_with_replacement
print(list(combinations_with_replacement(arr, 3)))