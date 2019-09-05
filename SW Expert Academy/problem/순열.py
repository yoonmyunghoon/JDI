def perm(n, k):
    if n == k:
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

arr = [1, 2, 3, 4]
perm(4, 0)
