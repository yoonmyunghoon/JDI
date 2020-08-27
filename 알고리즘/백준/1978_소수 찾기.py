import sys, math
sys.stdin = open("1978_소수 찾기.txt")

N = int(input())
data = list(map(int, input().split()))
Max = max(data)
prime = [1]*(Max+1)
prime[0] = 0
prime[1] = 0
for i in range(4, Max+1, 2):
    prime[i] = 0
for i in range(3, int(math.sqrt(Max))+1, 2):
    if prime[i] == 0:
        continue
    for j in range(i*i, Max+1, i*2):
        prime[j] = 0
cnt = 0
for n in data:
    if prime[n] == 1:
        cnt += 1
print(cnt)