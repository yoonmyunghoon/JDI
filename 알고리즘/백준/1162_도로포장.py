import sys
sys.stdin = open("1162_도로포장.txt")
# input = sys.stdin.readline


N, M, K = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    s, e, t = map(int, input().split())
    G[s].append([e, t])
    G[e].append([s, t])
print(N, M, K)
for g in G:
    print(g)
print()