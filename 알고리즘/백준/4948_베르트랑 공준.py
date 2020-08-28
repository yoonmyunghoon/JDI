import sys, math
sys.stdin = open("4948_베르트랑 공준.txt")

Max = 123456*2
data = [1]*(Max+1)
data[0] = 0
data[1] = 0
for i in range(4, Max+1, 2):
    data[i] = 0
for i in range(3, int(math.sqrt(Max))+1, 2):
    if data[i] == 0:
        continue
    for j in range(i*i, Max+1, i*2):
        data[j] = 0

while 1:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if data[i] == 1:
            cnt += 1
    print(cnt)

