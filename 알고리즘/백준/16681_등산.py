import sys
sys.stdin = open("16681_등산.txt")
# input = sys.stdin.readline


N, M, D, E = map(int, input().split())
H = list(map(int, input().split()))
H.insert(0, 0)
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b, n = map(int, input().split())
    G[a].append([b, n])
    G[b].append([a, n])

print(N, M, D, E)
print(H)
for i in G:
    print(i)
print()
