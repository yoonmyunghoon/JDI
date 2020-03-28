import sys
sys.stdin = open("2455_지능형기차.txt")

G = []
for i in range(4):
    a, b = map(int, input().split())
    G.append([a, b])
maximum = 0
for i in range(3):
    G[i+1][1] = G[i][1] - G[i+1][0] + G[i+1][1]
    if G[i+1][1] > maximum:
        maximum = G[i+1][1]
print(maximum)