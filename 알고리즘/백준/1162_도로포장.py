import sys, heapq, math
sys.stdin = open("1162_도로포장.txt")
# input = sys.stdin.readline


def dijkstra(start, graph):
    dist = [[math.inf for _ in range(N+1)] for _ in range(K+1)]
    heap = []
    cnt = 0
    dist[cnt][start] = 0
    heapq.heapify(heap)
    heapq.heappush(heap, [dist[cnt][start], start, cnt])
    while heap:
        pre_cost, pre_node, cnt = heapq.heappop(heap)
        if dist[cnt][pre_node] < pre_cost:
            continue
        for next_node, next_cost in graph[pre_node]:
            new_cost = pre_cost + next_cost
            if dist[cnt][next_node] > new_cost:
                dist[cnt][next_node] = new_cost
                heapq.heappush(heap, [dist[cnt][next_node], next_node, cnt])
            if cnt < K and dist[cnt+1][next_node] > pre_cost:
                dist[cnt + 1][next_node] = pre_cost
                heapq.heappush(heap, [dist[cnt+1][next_node], next_node, cnt+1])
    return dist


N, M, K = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    s, e, t = map(int, input().split())
    G[s].append([e, t])
    G[e].append([s, t])
results = dijkstra(1, G)
min_time = math.inf
for result in results:
    if result[N] < min_time:
        min_time = result[N]
print(min_time)


