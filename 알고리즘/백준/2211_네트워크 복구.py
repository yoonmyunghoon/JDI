import sys
sys.stdin = open("2211_네트워크 복구.txt")
# input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    A, B, C = map(int, input().split())
    G[A].append([B, C])

print(N, M)
for i in G:
    print(i)
print()

