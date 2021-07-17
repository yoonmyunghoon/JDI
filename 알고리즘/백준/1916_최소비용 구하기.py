import sys
import heapq
sys.stdin = open("1916_최소비용 구하기.txt")
# input = sys.stdin.readline


def dijkstra(graph, first, last):

    min_dist = [float('inf')] * (N+1)
    # N > M 인 경우 생각해보기, 전부다 Inf 가 아닐 수 있음, 이게 왜 문제가 되는지 생각해보자
    min_dist[first] = 0
    heap = []
    heapq.heappush(heap, (min_dist[first], first))

    while heap:
        now_min_dist, now = heapq.heappop(heap)
        if now in graph:
            for next_node, next_distance in graph[now].items():
                if now_min_dist + next_distance < min_dist[next_node]:
                    min_dist[next_node] = now_min_dist + next_distance
                    heapq.heappush(heap, (min_dist[next_node], next_node))
    return min_dist[last]


N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
G_dict = dict()
for i in range(M):
    s, e, w = map(int, input().split())
    # e가 2번 이상 들어올 수 있음, 이 경우에는 제일 가중치가 작은것만 취해야함, 생각해보자
    if s in G_dict:
        if e not in G_dict[s]:
            G_dict[s][e] = w
        else:
            if G_dict[s][e] > w:
                G_dict[s][e] = w
    else:
        G_dict[s] = dict()
        G_dict[s][e] = w
start, end = map(int, input().split())
print(dijkstra(G_dict, start, end))
