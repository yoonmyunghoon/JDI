import sys, heapq, math
sys.stdin = open("2211_네트워크 복구.txt")
# input = sys.stdin.readline

'''
1번이 슈퍼 컴퓨터
통신은 완전쌍방향 방식
모든 컴퓨터들은 이어져있어야함
슈퍼컴퓨터와 통신하는데 걸리는 시간을 최소로 해야함
각 컴퓨터들에 대해서 슈퍼컴퓨터와 통신 시간을 최소로하도록 경로를 만들어줘야함
최소 시간을 체크하면서 경로를 이어갈 떄, 해당 경로가 복구되야하는 경로이기 때문에 따로 List 에 기록해둬야함   
'''


def dijkstra(node, graph):
    dist = [math.inf]*(N+1)
    recover_path = [0]*(N+1)
    dist[node] = 0
    heap = []
    heapq.heappush(heap, [dist[node], node])
    while heap:
        now_w, now_node = heapq.heappop(heap)

        if dist[now_node] < now_w:
            continue

        for next_node, next_w in graph[now_node]:
            temp = now_w + next_w
            if temp < dist[next_node]:
                dist[next_node] = temp
                recover_path[next_node] = now_node
                heapq.heappush(heap, [dist[next_node], next_node])
    return recover_path


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    A, B, C = map(int, input().split())
    G[A].append([B, C])
    G[B].append([A, C])

result = dijkstra(1, G)
print(N-(result.count(0)-1))
for idx, v in enumerate(result):
    if v != 0:
        print(idx, v)
