import collections

def solution(n, edge):
    dic_G = {}
    for e in edge:
        if e[0]-1 in dic_G:
            dic_G[e[0]-1].append(e[1]-1)
        else:
            dic_G[e[0]-1] = [e[1]-1]
        if e[1]-1 in dic_G:
            dic_G[e[1]-1].append(e[0]-1)
        else:
            dic_G[e[1]-1] = [e[0]-1]

    deq = collections.deque()
    deq.append([0, 1])
    visited = [0] * n
    while deq:
        v, depth = deq.popleft()
        visited[v] = depth
        for w in dic_G[v]:
            if visited[w] == 0:
                visited[w] = depth+1
                deq.append([w, depth+1])
    return visited.count(max(visited))


ex_n = 6
ex_vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(ex_n, ex_vertex))