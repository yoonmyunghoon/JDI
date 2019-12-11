import sys
sys.stdin = open("메시지처리시간.txt")

a, b = map(int, input().split())
Big = []
M = []
for i in range(b):
    Big.append([])
for i in range(a):
    M.append(int(input()))
for i in range(a):
    Min = 10000
    Minid = 0
    for j in range(len(Big)):
        if Min > len(Big[j]):
            Min = len(Big[j])
            Minid = j
    for k in range(M[i]):
        Big[Minid].append(1)

print(len(max(Big)))