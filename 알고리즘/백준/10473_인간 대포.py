import math
import sys
import heapq
sys.stdin = open("10473_인간 대포.txt")
# input = sys.stdin.readline


'''
출발지, 도착지, 캐논 갯수, 캐논 위치 등을 저장함
일반적인 거리를 구하는 함수 하나 정의함
다익스트라 함수 정의함
각 정점들간의 시간을 기록해둠
'''


def cal_dist(ax, ay, bx, by):
    return ((ax-bx)**2+(ay-by)**2)**0.5


def dijkstra(node, graph):
    dist = [math.inf for _ in range(num+2)]
    dist[node] = 0

    heap = []
    heapq.heappush(heap, [dist[node], node])

    while heap:
        min_dist, now_node = heapq.heappop(heap)
        if dist[now_node] < min_dist:
            continue
        for next_node, next_dist in enumerate(graph[now_node]):
            tmp = next_dist + min_dist
            if tmp < dist[next_node]:
                dist[next_node] = tmp
                heapq.heappush(heap, [tmp, next_node])
    return dist


X, Y = map(float, input().split())
Px, Py = map(float, input().split())
num = int(input())
positions = [[X, Y]]
for i in range(num):
    A, B = map(float, input().split())
    positions.append([A, B])
positions.append([Px, Py])

time = [[] for _ in range(num+2)]
for i in range(num+2):
    for j in range(num+2):
        if i == 0 or i == num+1:
            time[i].append(cal_dist(positions[i][0], positions[i][1], positions[j][0], positions[j][1])/5)
        else:
            time_with_cannon = (abs(cal_dist(positions[i][0], positions[i][1], positions[j][0], positions[j][1])-50))/5+2
            time_without_cannon = cal_dist(positions[i][0], positions[i][1], positions[j][0], positions[j][1])/5
            time[i].append(min(time_with_cannon, time_without_cannon))
print(dijkstra(0, time)[-1])



