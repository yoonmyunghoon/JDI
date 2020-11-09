import sys
sys.stdin = open("DFS_BFS.txt")

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, V+1):
        if visited[w] == 0 and G[v][w] == 1:
            dfs(w)

V, E = map(int, input().split())
data = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0]*(V+1)
for i in range(len(data)//2):
    G[data[2 * i]][data[2 * i + 1]] = 1
    G[data[2 * i + 1]][data[2 * i]] = 1
for i in G:
    print(i)

dfs(1)