import sys
import heapq
sys.stdin = open("1238_파티.txt")
# input = sys.stdin.readline


def dijkstra(G, first):
    dist = [float('inf') for _ in range(N+1)]
    dist[first] = 0
    heap = []
    heapq.heappush(heap, [dist[first], first])

    while heap:
        min_dist, x = heapq.heappop(heap)
        for e, m in G[x]:
            if min_dist + m < dist[e]:
                dist[e] = min_dist + m
                heapq.heappush(heap, [dist[e], e])

    return dist


N, M, X = map(int, input().split())
data = [[] for _ in range(N+1)]
rev_data = [[] for _ in range(N+1)]
for i in range(M):
    s, e, m = map(int, input().split())
    data[s].append([e, m])
    rev_data[e].append([s, m])

dists = []
go_dist = dijkstra(data, X)
come_dist = dijkstra(rev_data, X)
for k in range(1, N+1):
    dists.append(come_dist[k] + go_dist[k])
print(max(dists))


