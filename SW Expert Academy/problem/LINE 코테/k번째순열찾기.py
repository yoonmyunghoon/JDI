import sys
sys.stdin = open("k번째순열찾기.txt")

def perm(n, k):
    if n == k:
        L.append(''.join(arr))
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

arr = list(map(str, input().split()))
find = int(input())
L = []
perm(len(arr), 0)
for i in range(len(L)-1):
    for j in range(i, len(L)):
        if int(L[i]) > int(L[j]):
            L[i], L[j] = L[j], L[i]
print(L[find-1])

