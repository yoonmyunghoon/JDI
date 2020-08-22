import sys, collections
sys.stdin = open("1697_숨바꼭질.txt")


def bfs(x):
    visited[x] = 1
    deq = collections.deque()
    deq.append(x)
    while 1:
        v = deq.popleft()
        if v == K:
            print(visited[v]-1)
            return
        for i in range(3):
            if i == 0:
                nv = v - 1
            elif i == 1:
                nv = v + 1
            else:
                nv = 2*v
            if 0 <= nv <= 100000 and visited[nv] == 0:
                deq.append(nv)
                visited[nv] = visited[v] + 1


N, K = map(int, input().split())
visited = [0]*100001
bfs(N)