import sys
sys.stdin = open("2293_동전.txt")

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
D = [0]*(k+1)
D[0] = 1
for x in range(n):
    for y in range(k+1):
        if coins[x] <= y:
            D[y] += D[y-coins[x]]
print(D[k])