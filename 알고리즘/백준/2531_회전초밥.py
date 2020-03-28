import sys
sys.stdin = open("2531_회전초밥.txt")

N, d, k, c = map(int, input().split())
chobabs = []
for i in range(N):
    chobabs.append(int(input()))
maximum = 0
for i in range(N):
    types = set()
    types.add(c)
    for j in range(k):
        if i+j >= N:
            types.add(chobabs[(i + j) % N])
        else:
            types.add(chobabs[(i + j)])
    if maximum < len(types):
        maximum = len(types)
print(maximum)