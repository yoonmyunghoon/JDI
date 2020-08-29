import sys
sys.stdin = open("1016_제곱 ㄴㄴ 수.txt")


Min, Max = map(int, input().split())
r_Max = int(Max**0.5)
prime = [1]*(r_Max+1)
prime[0] = 0
prime[1] = 0
for i in range(4, r_Max+1, 2):
    prime[i] = 0
for i in range(3, int(r_Max**0.5)+1, 2):
    if prime[i]:
        for j in range(i*i, r_Max+1, 2*i):
            prime[j] = 0

check = [1]*(Max-Min+1)
for j in range(2, r_Max+1):
    if prime[j] == 1:
        x_check = Min % (j*j)
        if x_check:
            for i in range(Min+(j*j-x_check), Max+1, j*j):
                check[i-Min] = 0
        else:
            for i in range(Min, Max+1, j*j):
                check[i-Min] = 0
print(sum(check))


