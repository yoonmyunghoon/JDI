import sys
sys.stdin = open("2531_회전초밥.txt")

N, d, k, c = map(int, input().split())
plate = []
check = [0]*(d+1)
check[c] += 1
for i in range(N):
    n = int(input())
    plate.append(n)
plate = plate*2
for i in range(0, k):
    check[plate[i]] += 1
result = d+1-check.count(0)
now = result
for i in range(1, N+1):
    check[plate[i-1]] -= 1
    if check[plate[i-1]] == 0:
        now -= 1
    check[plate[i+k-1]] += 1
    if check[plate[i+k-1]] == 1:
        now += 1
    if result < now:
        result = now
print(result)


