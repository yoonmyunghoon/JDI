import sys
sys.stdin = open("2904_수학은 너무 쉬워.txt")


def factorize(n):
    number = cards[n]
    while 1:
        if number == 1:
            break
        for i in range(Max+1):
            if check[i] == 1:
                if number%i == 0:
                    number = number//i
                    factors[n].append(i)
                    break


N = int(input())
cards = list(map(int, input().split()))
factors = [[] for _ in range(N)]
Max = max(cards)
counts = [0] * (Max+1)
check = [1] * (Max+1)
check[0] = 0
check[1] = 0
for i in range(4, Max+1, 2):
    check[i] = 0
for i in range(3, int(Max**0.5)+1, 2):
    if check[i]:
        for j in range(i*i, Max+1, 2*i):
            check[j] = 0
for i in range(N):
    factorize(i)
for i in range(N):
    for j in range(len(factors[i])):
        counts[factors[i][j]] += 1
GCM = []
GCM_num = 1
for i in range(Max+1):
    if counts[i] > 0:
        s = int(counts[i]//N)
        for ss in range(s):
            GCM.append(i)
            GCM_num *= i
        if counts[i] >= N:
            counts[i] = s
        else:
            counts[i] = 0
result = 0
for i in range(Max+1):
    if counts[i] > 0:
        for j in range(N):
            cnt = 0
            for k in range(len(factors[j])):
                if factors[j][k] == i:
                    cnt += 1
            if counts[i] > cnt:
                result += (counts[i] - cnt)
print(GCM_num, result)





