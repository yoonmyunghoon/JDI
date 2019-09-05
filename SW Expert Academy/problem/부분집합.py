def powerSet(n, k):
    if n == k:
        for i in range(n):
            if A[i] == 1:
                print(arr[i], end=' ')
        print()
    else:
        A[k] = 1
        powerSet(n, k+1)
        A[k] = 0
        powerSet(n, k+1)


arr = [1, 2, 3, 4]
A = [0]*4
powerSet(4, 0)