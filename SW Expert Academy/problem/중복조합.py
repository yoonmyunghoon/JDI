N = 4
arr = list(range(1, N+1))
T = [0] * 3
# 중복조합
def comb1(n, r):
    if r == 0:
        print(T)
    elif n == 0:
        return
    else:
        T[r-1] = arr[n-1]
        comb1(n, r-1)
        comb1(n-1, r)

comb1(N, 3)
print()

# 조합계산
def combcount(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return combcount(n-1, r-1) + combcount(n-1, r)
print(combcount(N, 3))