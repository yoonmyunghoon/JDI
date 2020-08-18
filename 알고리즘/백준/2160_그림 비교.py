import sys
sys.stdin = open("2160_그림 비교.txt")

N = int(input())
pictures = [[list(input()) for _ in range(5)] for _ in range(N)]
minimum = 100
c1, c2 = 0, 0

for i in range(len(pictures)):
    for j in range(i+1, N):
        dc = 0
        for a in range(5):
            for b in range(7):
                if pictures[i][a][b] != pictures[j][a][b]:
                    dc += 1
        if minimum > dc:
            minimum = dc
            c1, c2 = i, j

print(c1+1, c2+1)