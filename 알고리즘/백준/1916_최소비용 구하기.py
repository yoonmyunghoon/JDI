import sys
import heapq
sys.stdin = open("1916_최소비용 구하기.txt")
# input = sys.stdin.readline


def dijkstra(graph, first, last):

    min_dist = [float('inf')] * (N+1)
    min_dist[first] = 0
    heap = []
    heapq.heappush(heap, (min_dist[first], first))

    while heap:
        now_min_dist, now = heapq.heappop(heap)
        for next, next_distance in graph[now]:
            if now_min_dist + next_distance < min_dist[next]:
                min_dist[next] = now_min_dist + next_distance
                heapq.heappush(heap, (min_dist[next], next))
    return min_dist[last]


N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
for i in range(M):
    s, e, w = map(int, input().split())
    G[s].append((e, w))
start, end = map(int, input().split())
print(dijkstra(G, start, end))
