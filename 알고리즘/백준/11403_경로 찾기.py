import sys, collections
sys.stdin = open("11403_경로 찾기.txt")


def bfs(x):
    deque = collections.deque()
    deque.append(x)
    while deque:
        v = deque.popleft()
        for u in range(N):
            if G[v][u] == 1 and visited[u] == 0:
                deque.append(u)
                visited[u] += 1


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    visited = [0] * N
    bfs(i)
    for j in visited:
        print(j, end=' ')
    print()

