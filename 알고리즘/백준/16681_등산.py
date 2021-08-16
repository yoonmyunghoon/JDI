import sys, math, heapq
sys.stdin = open("16681_등산.txt")
# input = sys.stdin.readline
'''
집에서 갈 수 있는 경로들, 최소 거리 찾기
학교에서 갈 수 있는 경로들, 최소 거리 찾기
둘다 가능한 목표지점 찾기
가능한 목표지접 별로 가치를 계산해서 비교하기
'''


def dijkstra(start, graph):
    dist = [math.inf for _ in range(N+1)]
    dist[start] = 0
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, [dist[start], start])
    while heap:
        pre_dist, pre_node = heapq.heappop(heap)
        if pre_dist > dist[pre_node]:
            continue
        for next_node, next_dist in graph[pre_node]:
            if H[pre_node] >= H[next_node]:
                continue
            temp = pre_dist + next_dist
            if temp < dist[next_node]:
                dist[next_node] = temp
                heapq.heappush(heap, [temp, next_node])
    return dist


N, M, D, E = map(int, input().split())
H = list(map(int, input().split()))
H.insert(0, 0)
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b, n = map(int, input().split())
    G[a].append([b, n])
    G[b].append([a, n])
dist_from_home = dijkstra(1, G)
dist_from_school = dijkstra(N, G)
result = []
for i in range(N+1):
    if dist_from_home[i] != math.inf and dist_from_school[i] != math.inf:
        dist_home_to_school = dist_from_home[i] + dist_from_school[i]
        result.append(H[i]*E - dist_home_to_school*D)
if len(result) != 0:
    print(max(result))
else:
    print('Impossible')



