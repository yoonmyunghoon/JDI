import sys, math
sys.stdin = open("3896_소수 사이 수열.txt")

Max = 1299709
sq_Max = int(math.sqrt(Max))
data = [1]*(Max+1)
data[0] = 0
data[1] = 0
for i in range(4, Max+1, 2):
    data[i] = 0
for i in range(3, sq_Max+1, 2):
    if data[i] == 0:
        continue
    for j in range(i*i, Max+1, i*2):
        data[j] = 0

T = int(input())
for tc in range(T):
    k = int(input())
    if data[k] == 1:
        print(0)
    else:
        cnt = 0
        m = k
        p = k
        while data[m] == 0:
            cnt += 1
            m -= 1
        while data[p] == 0:
            cnt += 1
            p += 1
        print(cnt)