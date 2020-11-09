# 부분집합
arr = [1, 2, 3, 4]
A = [0]*4
def powerset(n, k):
    if n == k:
        for i in range(len(A)):
            if A[i] == 1:
                print(arr[i], end=' ')
        print()
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)
powerset(4, 0)

# 순열
arr1 = [1, 2, 3, 4]
def perm(n, k):
    if n == k:
        print(arr1)
    else:
        for i in range(k, n):
            arr1[i], arr1[k] = arr1[k], arr1[i]
            perm(n, k+1)
            arr1[i], arr1[k] = arr1[k], arr1[i]
perm(4, 0)
print()

# 순열(n개에서 r개 뽑고 순서 세우기)
arr11 = [1, 2, 3, 4]
K = [0]*3
def myprint(q):
    for i in range(q-1, -1, -1):
        print(K[i], end=' ')
    print()

def perm1(n, r):
    if r == 0:
        myprint(3)
    else:
        for i in range(n-1, -1, -1):
            arr11[i], arr11[n-1] = arr11[n-1], arr11[i]
            K[r-1] = arr11[n-1]
            perm1(n-1, r-1)
            arr11[i], arr11[n-1] = arr11[n-1], arr11[i]

perm1(4, 3)
print()

# 중복순열
arr111 = [1, 2, 3, 4]
P = [0]*3
def myprint2(q):
    for i in range(q-1, -1, -1):
        print(P[i], end=' ')
    print()

def perm2(n, r):
    if r == 0:
        myprint2(3)
    else:
        for i in range(n-1, -1, -1):
            arr111[i], arr111[n-1] = arr111[n-1], arr111[i]
            P[r-1] = arr111[n-1]
            perm2(n, r-1)
            arr111[i], arr111[n - 1] = arr111[n - 1], arr111[i]
perm2(4, 3)
print()

# 조합
arr2 = [1, 2, 3, 4]
T = [0]*3
def comb(n, r):
    if r == 0:
        print(T)
    elif n < r:
        return
    else:
        T[r-1] = arr2[n-1]
        comb(n-1, r-1)
        comb(n-1, r)
comb(4, 3)
print()

# 중복조합
arr2 = [1, 2, 3, 4]
T2 = [0]*3
def comb1(n, r):
    if r == 0:
        print(T2)
    elif n == 0:
        return
    else:
        T2[r-1] = arr2[n-1]
        comb1(n, r-1)
        comb1(n-1, r)
comb1(4, 3)
print()

# 조합 개수 세기
def cntcomb(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return cntcomb(n-1, r-1) + cntcomb(n-1, r)

print(cntcomb(4, 3))
