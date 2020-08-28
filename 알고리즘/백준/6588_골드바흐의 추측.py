import sys, math
sys.stdin = open("6588_골드바흐의 추측.txt")

Max = 1000000
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

while 1:
    n = int(input())
    if n == 0:
        break
    a = 0
    b = 0
    for i in range(3, Max//2+1, 2):
        if data[i] == 1 and data[n-i] == 1:
            a = i
            b = n - i
            break
    if a == 0 and b == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print('{} = {} + {}'.format(n, a, b))
