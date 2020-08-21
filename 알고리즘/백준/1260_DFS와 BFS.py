import sys, collections
sys.stdin = open("1260_DFS와 BFS.txt")


def dfs(x):
    visited[x] = 1
    print(x, end=' ')
    for i in G[x]:
        if visited[i] == 0:
            dfs(i)


def bfs(x):
    visited1[x] = 1
    deq = collections.deque()
    deq.append(x)
    while deq:
        v = deq.popleft()
        print(v, end=' ')
        for u in G[v]:
            if visited1[u] == 0:
                deq.append(u)
                visited1[u] = 1


N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [0]*(N+1)
visited1 = [0]*(N+1)
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
for i in range(len(G)):
    G[i].sort()
dfs(V)
print()
bfs(V)