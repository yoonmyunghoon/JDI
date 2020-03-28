import sys, collections
sys.stdin = open('DFS_BFS.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, V+1):
        if visited[w] == 0 and G[v][w] == 1:
            dfs(w)

# def bfs(v):
#     visited1[v] = 1
#     Q = [v]
#     while Q:
#         t = Q.pop(0)
#         print(t, end=' ')
#         for w in range(1, V+1):
#             if visited1[w] == 0 and G[t][w] == 1:
#                 visited1[w] = 1
#                 Q.append(w)

def bfs(v):
    visited1[v] = 1
    deq = collections.deque()
    deq.append(v)
    while deq:
        t = deq.popleft()
        print(t, end=' ')
        for w in range(1, V+1):
            if visited1[w] == 0 and G[t][w] == 1:
                visited1[w] = 1
                deq.append(w)

V, E = map(int, input().split())
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
data = list(map(int, input().split()))
visited = [0]*(V+1)
visited1 = [0]*(V+1)
for i in range(E):
    s = data[2*i]
    e = data[2*i+1]
    G[s][e] = 1
    G[e][s] = 1
for i in G:
    print(i)
print()

dfs(1)
print()
bfs(1)