import sys
sys.stdin = open("2038_골롱 수열.txt")

n = int(input())
data = [0]*(n+1)
data[1] = 1
k = 1
s = 1
e = 1
if n == 1:
    print(1)
else:
    while 1:
        k += 1
        s = e + 1
        data[s] = k
        e = e + data[k]
        if e >= n:
            print(k)
            break
        for i in range(s+1, e+1):
            data[i] = k