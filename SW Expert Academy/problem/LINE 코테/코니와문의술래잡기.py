import sys
sys.stdin = open("코니와문의술래잡기.txt")

def perm(n, k):
    if n == k:
        arrset.add(''.join(arr))
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

n, m = map(int, input().split())
x, y = map(int, input().split())
arr = []
arrset = {0}
if x > n or y > m:
    print('fail')
else:
    print(x+y)
    for i in range(x):
        arr.append('1')
    for j in range(y):
        arr.append('0')
    perm(x+y, 0)
    print(len(arrset)-1)



