import sys
sys.stdin = open("15649_N과M(1).txt")

def dfs(n, m):
    if m == M:
        for i in range(m):
            print(T[i], end=' ')
        print()
        return
    for i in range(n):
        if visited[i] == 0:
            T[m] = arr[i]
            visited[i] = 1
            dfs(n, m+1)
            visited[i] = 0

N, M = map(int, input().split())
visited = [0]*N
arr = list(range(1, N+1))
T = [0]*M
dfs(N, 0)
