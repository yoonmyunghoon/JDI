import collections

def solution(n, edge):
    G = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0]*n

    def bfs(x):
        visited[x] = 1
        deq = collections.deque()
        deq.append(x)
        maximum = 0
        while deq:
            v = deq.popleft()
            if maximum < visited[v]:
                maximum = visited[v]
            for w in range(n):
                if visited[w] == 0 and G[v][w] == 1:
                    visited[w] = visited[v] + 1
                    deq.append(w)
        return maximum

    for e in edge:
        G[e[0]-1][e[1]-1] = 1
        G[e[1]-1][e[0]-1] = 1
    return visited.count(bfs(0))


ex_n = 6
ex_vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(ex_n, ex_vertex))