import time
from time import strftime

start_time = time.time()

import sys
import collections
sys.stdin = open('1249_보급로.txt', 'r')
T = int(input())

def check(x, y):
    if x < 0 or y < 0 or x > N-1 or y > N-1: return False
    if visit[x][y] : return False
    return True

def bfs(x,y):
    dx = [0, 0 ,1, -1]
    dy = [1, -1, 0, 0]
    deq = collections.deque()
    dist[x][y] = 0
    deq.append([x, y])    # enQ
    while len(deq) != 0:
        x, y = deq.popleft()  #deQ
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny) and dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                dist[nx][ny] = dist[x][y] + arr[nx][ny]
                deq.append([nx, ny])  # enQ

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    heap = []

    bfs(0,0)
    print("#{} {}".format(tc+1, dist[N-1][N-1]))
print(time.time() - start_time, 'seconds')