import sys
sys.stdin = open("16681_등산.txt")
# input = sys.stdin.readline
'''
집에서 갈 수 있는 경로들, 최소 거리 찾기
학교에서 갈 수 있는 경로들, 최소 거리 찾기
둘다 가능한 목표지점 찾기
가능한 목표지접 별로 가치를 계산해서 비교하기
'''

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
