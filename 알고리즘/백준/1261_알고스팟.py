import sys
import heapq
sys.stdin = open("1261_알고스팟.txt")
# input = sys.stdin.readline


def dijkstra(G):
    dist = [[float('inf') for _ in range(M)] for _ in range(N)]
    dist[0][0] = 0
    heap = []
    heapq.heappush(heap, [dist[0][0], 0, 0])
    while heap:
        min_dist, x, y = heapq.heappop(heap)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if min_dist + G[nx][ny] < dist[nx][ny]:
                    dist[nx][ny] = min_dist + G[nx][ny]
                    heapq.heappush(heap, [dist[nx][ny], nx, ny])
    return dist[N-1][M-1]


M, N = map(int, input().split())
Room = [list(map(int, input())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
print(dijkstra(Room))




