import sys, collections
sys.stdin = open("11724_연결 요소의 개수.txt")


# dfs
def dfs(v):
    visited[v] = 1
    for u in graph[v]:
        if visited[u] == 0:
            dfs(u)


# bfs
def bfs(v):
    visited[v] = 1
    deque = collections.deque()
    deque.append(v)
    while deque:
        x = deque.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                deque.append(i)
                visited[i] = 1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        # bfs or dfs
        dfs(i)
        cnt += 1
print(cnt)