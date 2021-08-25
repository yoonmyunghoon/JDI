import sys, heapq, math
sys.stdin = open("1162_도로포장.txt")
# input = sys.stdin.readline


def dijkstra(start, graph):
    dist = [[math.inf for _ in range(K+1)] for _ in range(N+1)]
    heap = []
    cnt = 0
    dist[start][cnt] = 0
    heapq.heapify(heap)
    heapq.heappush(heap, [dist[start][cnt], start, cnt])
    while heap:
        pre_cost, pre_node, cnt = heapq.heappop(heap)
        if dist[pre_node][cnt] < pre_cost:
            continue
        for next_node, next_cost in graph[pre_node]:
            new_cost = pre_cost + next_cost
            if dist[next_node][cnt] > new_cost:
                dist[next_node][cnt] = new_cost
                heapq.heappush(heap, [new_cost, next_node, cnt])
            if cnt < K and dist[next_node][cnt+1] > pre_cost:
                dist[next_node][cnt+1] = pre_cost
                heapq.heappush(heap, [pre_cost, next_node, cnt+1])
    return dist


N, M, K = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    s, e, t = map(int, input().split())
    G[s].append([e, t])
    G[e].append([s, t])
result = dijkstra(1, G)
print(min(result[N]))


