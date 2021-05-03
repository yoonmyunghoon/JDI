import sys
import heapq
sys.stdin = open("4485_녹색 옷 입은 애가 젤다지?.txt")
# input = sys.stdin.readline


def dijkstra(graph, num):
    dist = [[float('inf') for _ in range(num)] for _ in range(num)]
    dist[0][0] = graph[0][0]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    heap = []
    heapq.heappush(heap, [dist[0][0], 0, 0])

    while heap:
        min_dist, x, y = heapq.heappop(heap)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < num and 0 <= ny < num:
                if min_dist + graph[nx][ny] < dist[nx][ny]:
                    dist[nx][ny] = min_dist + graph[nx][ny]
                    heapq.heappush(heap, [dist[nx][ny], nx, ny])
    return dist[num-1][num-1]


n = 0
while 1:
    n+=1
    N = int(input())
    if N == 0:
        break

    Cave = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {n}: {dijkstra(Cave, N)}')
