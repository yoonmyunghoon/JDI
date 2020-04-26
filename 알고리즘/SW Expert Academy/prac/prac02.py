# 조합
# def comb(n, r):
#     if r == 0:
#         print(T)
#     elif n < r:
#         return
#     else:
#         T[r-1] = A[n-1]
#         comb(n-1, r-1)
#         comb(n-1, r)
#
# A = [1, 2, 3, 4, 5]
# T = [0]*3
# comb(5, 3)

# 순열
# def perm(n, k):
#     if n == k:
#         print(arr)
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n, k+1)
#             arr[k], arr[i] = arr[i], arr[k]
# arr = [1, 2, 3, 4, 5]
# perm(5, 0)

# 부분집합
# def powerSet(n, k):
#     if n == k:
#         for i in range(n):
#             if A[i] == 1:
#                 print(arr[i], end=' ')
#         print()
#     else:
#         A[k] = 1
#         powerSet(n, k+1)
#         A[k] = 0
#         powerSet(n, k+1)
#
# arr = [1, 2, 3, 4, 5]
# A = [0]*5
# powerSet(5, 0)