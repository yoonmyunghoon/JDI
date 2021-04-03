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

AB = dict()
for a in A:
    for b in B:
        if AB.get(a+b):
            AB[a+b] += 1
        else:
            AB[a+b] = 1
cnt = 0
for c in C:
    for d in D:
        if AB.get(-(c+d)):
            cnt += AB.get(-(c+d))

print(cnt)




