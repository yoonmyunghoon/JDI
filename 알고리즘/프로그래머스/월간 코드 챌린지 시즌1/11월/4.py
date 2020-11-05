def solution(t):
    answer = 0
    G = {}
    visited = [0]*(len(t)+1)
    for a, b in t:
        if a in G:
            G[a].append(b)
        else:
            G[a] = [b]
        if b in G:
            G[b].append(a)
        else:
            G[b] = [a]
    print(G)

    def dfs(x, cnt):
        visited[x] += 1
        for w in G[x]:
            if len(G[w]) == 1:
                if visited[w] == 0:
                    dfs(w, cnt + 1)
                    visited[w] -= 1
                else:
                    print(cnt)
                    return
            else:
                if visited[w] < 2:
                    dfs(w, cnt+1)
                    visited[w] -= 1
                else:
                    print(cnt)
                    return

    for i in range(len(t)+1):
        if len(G[i]) == 1 and visited[i] == 0:
            dfs(i, 1)
    print(visited)


    return answer

ex_t = [[5,1],[2,5],[3,5],[3,6],[2,4],[4,0]]
print(solution(ex_t))