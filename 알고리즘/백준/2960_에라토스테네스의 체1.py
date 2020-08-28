import sys, math
sys.stdin = open("2960_에라토스테네스의 체.txt")

N, K = map(int, input().split())
check = [1]*(N+1)
check[0] = 0
check[1] = 0
output = []
for i in range(2, N+1):
    if check[i] == 1:
        output.append(i)
        check[i] = 0
        for j in range(i*2, N+1, i):
            if check[j] == 1:
                output.append(j)
                check[j] = 0
print(output[K-1])