N = 4
arr = list(range(1, N+1))

q = 3
T = [0] * q
def myprint(q):
    for i in range(q-1, -1, -1):
        print(T[i], end=' ')
    print()

#순열(n개중에서 r를 뽑아서 순서정하기)
def perm2(n, r):
    if r == 0:
        myprint(q)
        return
    else:
        for i in range(n-1, -1, -1):
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
            T[r-1] = arr[n-1]
            perm2(n-1, r-1)
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
perm2(N, 3)
print()

#중복순열(n개중에서 r를 뽑아서 중복포함해서 순서정하기)
def perm3(n, r):
    if r == 0:
        myprint(q)
        return
    else:
        for i in range(n-1, -1, -1):
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
            T[r-1] = arr[n-1]
            perm3(n, r-1)
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
perm3(N, 3)
print()

