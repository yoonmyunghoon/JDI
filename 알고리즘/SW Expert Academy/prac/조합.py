# def comb(n, r, q):
#     if r == 0:
#         print(T)
#     elif n < r:
#         return
#     else:
#         T[r-1] = A[n-1]
#         comb(n-1, r-1, q)
#         comb(n-1, r, q)
#
# A = [1, 2, 3, 4]
# T = [0]*3
# comb(4, 3, 3)

# q 없어도 됨
def comb(n, r):
    if r == 0:
        print(T)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

A = [1, 2, 3, 4]
T = 3 * [0]
comb(4, 3)