import sys
import heapq
sys.stdin = open('1753_최단경로.txt')
# input = sys.stdin.readline


def dijkstra(graph, first):
    dist = [float("inf")] * (V+1)
    dist[first] = 0

    heap = []
    heapq.heappush(heap, (dist[first], first))

    while heap:
        min_dist, node = heapq.heappop(heap)
        for v, w in graph[node]:
            if dist[node] + w < dist[v]:
                dist[v] = dist[node] + w
                heapq.heappush(heap, (dist[v], v))
    return dist


V, E = map(int, input().split())
K = int(input())
data = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    data[u].append((v, w))
dist = dijkstra(data, K)
for i in range(1, len(dist)):
    if dist[i] == float("inf"):
        print("INF")
    else:
        print(dist[i])



