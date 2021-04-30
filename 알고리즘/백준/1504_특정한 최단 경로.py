import sys
import heapq
sys.stdin = open("1504_특정한 최단 경로.txt")
# input = sys.stdin.readline


N, E = map(int, input().split())
data = [[] for _ in range(N+1)]


def dijkstra(graph, first):
    dist = [float("inf")] * (N+1)
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


for i in range(E):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))

v1, v2 = map(int, input().split())

dist1 = dijkstra(data, 1)
dist2 = dijkstra(data, N)
dist3 = dijkstra(data, v1)
a = dist1[v1] # 3
b = dist1[v2] # 5
c = dist2[v1] # 4
d = dist2[v2] # 1
e = dist3[v2] # 3
result = min(a+d+e, c+b+e)
if result == float("inf"):
    print(-1)
else:
    print(min(a+d+e, c+b+e))



# 1 - 2 : 3
# 1 - 3 : 5
# 4 - 2 : 4
# 4 - 3 : 1
# 2 - 3 : 3

# 1 - 2 - 3 - 4 : 7
# 4 - 2 - 3 - 1 : 12



