import collections


def solution(n, computers):

    def bfs(x):
        visited[x] = cnt
        deq = collections.deque()
        deq.append(x)
        while deq:
            v = deq.popleft()
            for w in range(n):
                if visited[w] == 0 and computers[v][w] == 1:
                    visited[w] = cnt
                    deq.append(w)

    visited = [0] * n
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            cnt += 1
            bfs(i)
    return cnt


ex_n = 3
ex_computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(ex_n, ex_computers))