import sys
sys.stdin = open('7453_합이 0인 네 정수.txt')
input = sys.stdin.readline

N = int(input())
A = []
B = []
C = []
D = []
for i in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
for a in A:
    for b in B:
        AB.append(a+b)

CD = []
for c in C:
    for d in D:
        CD.append(c+d)

AB.sort()
CD.sort(reverse=True)

AB_idx = CD_idx = 0
len_list = N*N
cnt = 0

while AB_idx < len_list and CD_idx < len_list:
    temp = AB[AB_idx] + CD[CD_idx]
    if temp > 0:
        CD_idx += 1
    elif temp < 0:
        AB_idx += 1
    else:
        i = AB_idx
        j = CD_idx
        while i < len_list and AB[AB_idx] == AB[i]:
            i += 1
        while j < len_list and CD[CD_idx] == CD[j]:
            j += 1
        cnt += (i-AB_idx)*(j-CD_idx)
        AB_idx = i
        CD_idx = j
print(cnt)






