arr = [1, 2, 3, 4]
q = 3
T = [0]*q

def myprint(q):
    for i in range(q-1, -1, -1):
        print(T[i], end= ' ')
    print()

def perm(n, r):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            arr[i], arr[n-1] = arr[n-1], arr[i]
            T[r-1] = arr[n-1]
            perm(n, r-1)
            arr[i], arr[n - 1] = arr[n - 1], arr[i]

perm(4, 3)